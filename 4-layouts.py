'''
sketch about layouts

https://www.pythonguis.com/tutorials/pyqt-layouts/

'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, QStackedLayout, QTabWidget
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    '''
    a widget with specific background color.
    '''
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class SingleWin(QMainWindow):
    '''
    one widget with red background
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = Color("red")
        self.setCentralWidget(widget)

class Layout_Colorful_ver(QMainWindow):
    '''
    A layout box with three vertically arranged widgets in different colors.

    ordered from top to bottom.
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class Layout_Colorful_hori(QMainWindow):
    '''
    A layout box with three vertically arranged widgets in different colors,

    ordered from left to right.
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QHBoxLayout()              # changing from `QVBoxLayout` to `QHBoxLayout`
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class Nesting_Layouts(QMainWindow):
    '''
    Nesting layouts.
    ┌───────────────────────────────┐
    │          (Margins)            │  ↑ top margin
    │   ┌───────────────────────┐   │
    │   │      (Spacing)        │   │
    │   │   [Widget1]           │   │
    │   │      (Spacing)        │   │  ← spacing between widgets
    │   │   [Widget2]           │   │
    │   │      (Spacing)        │   │
    │   │   [Widget3]           │   │
    │   └───────────────────────┘   │  ↓ bottom margin
    │                               │
    └───────────────────────────────┘
    .setContentsMargins(left, top, right, bottom)
    .setSpacing(1) # the spacing is minimum spacing
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout2.setContentsMargins(0,0,0,0)
        layout2.setSpacing(20)

        layout2.addWidget(Color('red'))
        layout2.addWidget(QPushButton('Button1'))
        layout2.addWidget(QPushButton('Button2'))

        layout1.addWidget(Color('red'))
        layout1.addLayout(layout2)          # Notice the order of this
        layout1.addWidget(Color('green'))
        layout1.addWidget(Color('blue'))
        widget = QWidget()
        widget.setLayout(layout1)
        

        self.setCentralWidget(widget)

class GridLayout(QMainWindow):
    '''
    Grid layout
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout1 = QGridLayout()
    
        layout1.addWidget(Color('red'), 0, 0)
        layout1.addWidget(Color('green'), 1, 0)
        layout1.addWidget(Color('blue'), 1, 1)
        widget = QWidget()
        widget.setLayout(layout1)
        

        self.setCentralWidget(widget)

class StackedLayout(QMainWindow):
    '''
    StackedLayout:
    All widgets are stacked in the same position. The earliest widget added in code is assigned index 0, and only the widget at index 0 is visible by default. To override this behavior, explicitly set the displayed widget using .setCurrentIndex(0).
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QStackedLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))
        layout.setCurrentIndex(2)           # set visible widget into the blue one

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class Tab_like(QMainWindow):
    '''
    layout1: Contains layout2 and layout3
    layout2: Contains three color widget in different color
    layout3: Contains three QPushButton who can change the top visible color widget
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        self.layout3 = QStackedLayout()

        bt1 = QPushButton('Blue')
        bt2 = QPushButton('Red')
        bt3 = QPushButton('Green')

        bt1.clicked.connect(self.SetBlue)
        bt2.clicked.connect(self.SetRed)
        bt3.clicked.connect(self.SetGreen)

        layout2.addWidget(bt1)
        layout2.addWidget(bt2)
        layout2.addWidget(bt3)

        self.layout3.addWidget(Color("red"))
        self.layout3.addWidget(Color("green"))
        self.layout3.addWidget(Color("blue"))

        layout1.addLayout(layout2)
        layout1.addLayout(self.layout3)

        widget = QWidget()
        widget.setLayout(layout1)

        self.setCentralWidget(widget)

    def SetRed(self):
        self.layout3.setCurrentIndex(0)
    def SetGreen(self):
        self.layout3.setCurrentIndex(1)
    def SetBlue(self):
        self.layout3.setCurrentIndex(2)

class TabWidget(QMainWindow):
    '''
    Using the Built-in widget `QTabWidget`
    '''
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.South)
        tabs.setDocumentMode(True) # Only valid on MacOS
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)

app = QApplication(sys.argv)

window = TabWidget()
window.show()

app.exec()

