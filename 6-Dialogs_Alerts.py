'''
About Dialog and Alerts

https://www.pythonguis.com/tutorials/pyqt-dialogs/
'''
import sys

from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel,
    QMessageBox,
    )

class CustomDialog(QDialog):
    '''
    About QDialogButtonBox:
        you can use QButton here, but it is NOT RECOMMENDED

    Button signals:
        code blow is needed to make the buttons effect:
        ```
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        ```

    '''
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("HELLO!")

        # more button could be found at https://doc.qt.io/qt-6/qdialogbuttonbox.html#StandardButton-enum
        QBtn = QDialogButtonBox.Cancel | QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class Dialog(QMainWindow):
    '''
    Waring: the Dialog here will blocks the main thread when executing,
    so put it into another thread later
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        # pass the parent and dialog window will appear at the same position with parent, not elsewhere
        dlg = CustomDialog(self)
        dlg.exec()

class MsgBox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        # https://doc.qt.io/qt-6/qmessagebox.html#StandardButton-enum
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # https://doc.qt.io/qt-6/qmessagebox.html#icon-prop
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Ok:
            print("OK!")

class SimpleMsgBox(QMainWindow):
    '''
    simpler QMessageBox, predefined message box
    https://doc.qt.io/qt-6/qmessagebox.html#severity-levels-and-the-icon-and-pixmap-properties
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        button = QMessageBox.warning(
            self,
            "Question dialog",
            "The longer message",
        )

        if button == QMessageBox.Ok:
            print("OK!")

class SimpleMsgBox(QMainWindow):
    '''
    The button and default button can be changed
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore, # button
            defaultButton=QMessageBox.Discard,                                      # default button
        )

        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")

app = QApplication(sys.argv)
window = SimpleMsgBox()
window.show()
app.exec()