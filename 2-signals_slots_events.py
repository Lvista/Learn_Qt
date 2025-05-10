'''
A sketch about signals, slots and events.

https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QMenu, QAction
from PyQt5.QtCore import Qt
from random import choice


window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class Usecase0(QMainWindow):
    '''
    usecase0: button click
    '''
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Press Me!")
        self.setWindowTitle("Nomal button")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        '''button pressing event
        '''
        print("Clicked!")

class Usecase1(QMainWindow):
    '''
    usecase1: one pressed button
    '''
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Press Me!")
        self.setWindowTitle("one pressed button")
        self.button_is_checked = None
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.setChecked(False)
        self.setCentralWidget(self.button)

    def the_button_was_toggled(self, checked):
        '''button pressing event

        show the state of check, storing it into `self.button_is_checked`
        '''
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
        self.setWindowTitle("A new window title")
        self.button_is_checked = self.button.isChecked()
        print("Checked?", self.button_is_checked)
        
class Usecase2(QMainWindow):
    '''
    usecase2: button click and changing the title
    '''
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Press Me!")
        self.setWindowTitle("title singnal")
        self.button.clicked.connect(self.the_button_was_clicked_with_title_changing)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setCentralWidget(self.button)

    def the_button_was_clicked_with_title_changing(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)
    
    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)

class Usecase3(QMainWindow):
    '''
    usecase3: label is changing along with the edit_box
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test changing")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

class Usecase4(QMainWindow):
    '''
    usecase4: mouse click event
    '''
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setMouseTracking(True)         # both is need to be set, themare parent ralationship
        self.label.setMouseTracking(True)
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        match e.button():
            case Qt.LeftButton: self.label.setText("mousePressEvent LEFT")
            case Qt.MiddleButton: self.label.setText("mousePressEvent MIDDLE")
            case Qt.RightButton: self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        match e.button():
            case Qt.LeftButton: self.label.setText("mouseReleaseEvent  LEFT")
            case Qt.MiddleButton: self.label.setText("mouseReleaseEvent  MIDDLE")
            case Qt.RightButton: self.label.setText("mouseReleaseEvent  RIGHT")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

class Usecase5(QMainWindow):
    '''
    usecase5: context menus
    '''
    def __init__(self):
        super().__init__()
        # approch1: overriding the contextMenuEvent
        pass
        # aprroch2: set to `CustomContextMenu` and connect to custom function
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    # approch1: overriding the contextMenuEvent
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

    # aprroch2: set to `CustomContextMenu` and connect to custom function
    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))
    
class Usecase6(QMainWindow):
    '''
    usecase5: context menus
    '''
    def __init__(self):
        super().__init__()
        self.button = CustomButton("click me!", self)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        print("Window Mouse pressed event!")

class CustomButton(QPushButton):

    def mousePressEvent(self, e):
        print("button Mouse pressed event!")
        e.ignore()
        # e.accept()                        # How is the deviation

class MainWindow():
    def __init__(self, num) -> None:
            match num:
                case 0: # button click
                    self.window = Usecase0()
                case 1: # one pressed button
                    self.window = Usecase1()
                case 2: # button click and changing the title
                    self.window = Usecase2()
                case 3: # connect one widget's signal to another widget's slot
                    self.window = Usecase3()
                case 4: # mouse click event
                    self.window = Usecase4()
                case 5: # context menus
                    self.window = Usecase5()
                case 6: # event hierarchy
                    self.window = Usecase6()

    def show(self):
        self.window.show()


def main():
    '''
    main function
    '''
    app = QApplication(sys.argv)

    # change the number to show different usecase
    window = MainWindow(6)
    window.show()

    app.exec()

if __name__ == '__main__':
        main()
