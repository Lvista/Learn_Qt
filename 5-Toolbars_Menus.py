'''
Defining toolbars, menus and keyboard shortcuts with QAction

https://www.pythonguis.com/tutorials/pyqt-actions-toolbars-menus/

'''
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QCheckBox,
    QPushButton,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    
)


class AddToolbar(QMainWindow):
    '''
    Derectly adding toolbar from parent object

    Note:
    Right-click the name to trigger a context menu and toggle the bar off,
    but unfortunately once you do it, there is now no way to re-add it.
    So keep one toolbar un-removeable, or provide an alternative interface in the menus to turn toolbars on and off.
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome App")

        toolbar = QToolBar('toolbar1')
        self.addToolBar(toolbar)

class Toolbar_with_Action(QMainWindow):
    '''
    Add some widget into toolbar.
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))     # Icon size
        # toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # style
        self.addToolBar(toolbar)

        # Bug button
        button_action = QAction(QIcon("bug.png"), "Your button", self)            # (name, icon, parent_QObject)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.toolbar_button_clicked)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        
        # add a separator bar
        toolbar.addSeparator()

        # Second Bug button
        button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.toolbar_button_clicked)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        # Text Label
        toolbar.addWidget(QLabel("Hello"))
        # CheckBox
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))                     # status bar will show when your mouse over the toolbar button

    def toolbar_button_clicked(self, s):
        print("click", s)

class Menu(QMainWindow):
    '''
    Menu Bar
        menu = self.menuBar()
        file_menu = menu.addMenu("&File") # name and hotkey whith is 'F' here
    
    Add items:
        menu.addAction(QAction)
    Add submenu:
        file_submenu = file_menu.addMenu("Submenu")
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))     # Icon size
        # toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # style
        self.addToolBar(toolbar)

        # Bug button
        button_action = QAction(QIcon("bug.png"), "Your button", self)            # (name, icon, parent_QObject)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.toolbar_button_clicked)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        
        # add a separator bar
        toolbar.addSeparator()

        # Second Bug button
        button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.toolbar_button_clicked)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        # Text Label
        toolbar.addWidget(QLabel("Hello"))
        # CheckBox
        toolbar.addWidget(QCheckBox())

        # ---------------menuBar------------------
        menu = self.menuBar()
        
        # add 'file' into menubar
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)          # Add button1 into menu
        file_menu.addSeparator()
        file_menu.addAction(button_action2)         # Add button2 into menu
        file_submenu = file_menu.addMenu("Submenu") # sub menu
        file_submenu.addAction(button_action2)

        self.setStatusBar(QStatusBar(self))                     # status bar will show when your mouse over the toolbar button

    def toolbar_button_clicked(self, s):
        print("click", s)

class Shortcut(QMainWindow):
    '''
    shortcut:
        button_action.setShortcut(QKeySequence("Ctrl+p"))
    Note:
        Here is also a effect approch, but previous one is recommanded for the operating system standards
        ```
        button_action.setShortcut("Ctrl+p")
        ```
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        # toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(toolbar)

        # Bug button
        button_action = QAction(QIcon("bug.png"), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.toolbar_button_clicked)
        button_action.setCheckable(True)
        button_action.setShortcut(QKeySequence("Ctrl+p"))              # set shortcut
        toolbar.addAction(button_action)
        
        # add a separator bar
        toolbar.addSeparator()

        # Second Bug button
        button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.toolbar_button_clicked)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        # Text Label
        toolbar.addWidget(QLabel("Hello"))
        # CheckBox
        toolbar.addWidget(QCheckBox())

        menu = self.menuBar()
        
        # add 'file' into menubar
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

        self.setStatusBar(QStatusBar(self))

    def toolbar_button_clicked(self, s):
        print("click", s)

app = QApplication([])
window = Shortcut()
window.show()
app.exec()