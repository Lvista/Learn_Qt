'''
sketch about widgets

https://www.pythonguis.com/tutorials/pyqt-basic-widgets/

| Widget         | What it does                            |
|----------------|-----------------------------------------|
| QCheckbox      | A checkbox                              |
| QComboBox      | A dropdown list box                     |
| QDateEdit      | For editing dates and datetimes         |
| QDateTimeEdit  | For editing dates and datetimes         |
| QDial          | Rotatable dial                          |
| QDoubleSpinbox | A number spinner for floats             |
| QFontComboBox  | A list of fonts                         |
| QLCDNumber     | A quite ugly LCD display                |
| QLabel         | Just a label, not interactive           |
| QLineEdit      | Enter a line of text                    |
| QProgressBar   | A progress bar                          |
| QPushButton    | A button                                |
| QRadioButton   | A toggle set, with only one active item |
| QSlider        | A slider                                |
| QSpinBox       | An integer spinner                      |
| QTimeEdit      | For editing times                       |

'''

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
    QDial,
)

class Label(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        widget = QLabel("1")  # The label is created with the text 1.
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        widget.setPixmap(QPixmap('./fig/otje.webp'))
        # widget.setScaledContents(True)

        self.setCentralWidget(widget)

class Figure(QMainWindow):
    def __init__(self):
        super().__init__()

        pixmap  = QPixmap()
        pixmap.load('./fig/otje.webp')
        # widget.setScaledContents(True)

        label = QLabel(self) # figure need to be load upon the label widget
        label.setPixmap(pixmap)

        self.setCentralWidget(label)

class Checkbox(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QCheckBox()
        widget.setCheckState(Qt.Checked)
        '''
        The box could be set to tristate using either of the two approaches below. 
        
        setTriState(True)
        widget.setCheckState(Qt.PartiallyChecked)
        '''
        widget.setChecked(False)
        widget.setText("This is a checkbox")

        self.setCentralWidget(widget)

class ComboBox(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QComboBox()
        widget.addItems(["one","two","three"])
        '''options
        - Insert:
            widget.setEditable(True)
            widget.setInsertPolicy(QComboBox.InsertAlphabetically)  # sort option
            widget.setMaxCount(10)                                  # max number of items
         
        see more:
        https://www.pythonguis.com/docs/qcombobox/#menu
        - 
        '''
        widget.currentIndexChanged.connect(self.index_changed)

        self.setCentralWidget(widget)

    def index_changed(self, index):
        print(index)

class ListWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self.index_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i): # Not an index, i is a QListWidgetItem
        print(i.text())

class LineEdit(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")


        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed) # triggered when the selection changs
        widget.textChanged.connect(self.text_changed)           # triggered when the text is changed
        widget.textEdited.connect(self.text_edited)             # triggered when the text is changed only by user

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

class QSpinBox_QDoubleSpinBox(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QSpinBox()
        # Or: widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)

        widget.setSingleStep(3)  # Or e.g. 0.5 for QDoubleSpinBox
        widget.valueChanged.connect(self.value_changed)
        widget.lineEdit().setReadOnly(True) # set box to set-read only

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

class Slider(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QDoubleSlider()

        # setting
        # widget = QSlider(Qt.Vertical)
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)
        widget.setSingleStep(3)

        # signals
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.value_changed)
        widget.sliderPressed.connect(self.value_changed)
        widget.sliderReleased.connect(self.value_changed)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        pass

class Dial(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.value_changed)
        widget.sliderPressed.connect(self.value_changed)
        widget.sliderReleased.connect(self.value_changed)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

app = QApplication(sys.argv)
window = Dial()
window.show()
app.exec()