'''
The first sketch about https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize, Qt
    

class MainWindow(QMainWindow):
    '''
    The main window class inherits from QMainWindow.
    
    This class creates a basic application window that includes a button as the central control.
    It provides the main interface framework of the application, which can be further expanded to add more features.
    
    para:
        None
        
    method:
        __init__: Initialize the main window, set the window title and basic UI elements
    '''
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)

def main():
    '''
    main function

    @retval None: need restert
    0: exit OK
    other: error
    '''
    ret = 0
    app = QApplication(sys.argv)            # 创建主线程实例
    # window = QPushButton("Push Me")
    window = MainWindow()                  # Create a Qt widget, which will be our window.
    window.show()                       # IMPORTANT!!!!! Windows are hidden by default.
    app.exec()                          # Start the event loop.
    return 0
    # return ret


if __name__ == '__main__':
    while 1:
        ret = main()
        break
        if not ret is None:
            break
        restart_program()
    print("-- program exit, code:", ret)
    sys.exit(ret)
