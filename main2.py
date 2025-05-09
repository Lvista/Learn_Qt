import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize, Qt
    

class MainWindow(QMainWindow):
    '''
    主窗口类，继承自 QMainWindow。
    
    这个类创建了一个基本的应用程序窗口，包含一个按钮作为中央控件。
    它提供了应用程序的主界面框架，可以进一步扩展添加更多功能。
    
    属性:
        None
        
    方法:
        __init__: 初始化主窗口，设置窗口标题和基本UI元素
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
    主函数

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
    main()
