"""
Short sketch about QPropertyAnimation

change the class name at the bottom of the file to run the sketch:
```
window = AnimatedBarWidget() # change this
```
"""
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame
from PyQt5.QtCore import QPropertyAnimation, QRect, Qt, pyqtProperty, QLine
from PyQt5.QtGui import QPainter, QColor, QPen


class AnimatedBarWidget(QWidget):
    """
    An example generated by DeepSeek.

    bar_rect is a QLine object, which is not a valid type for QPropertyAnimation.
    So creating a custom property `barGeometry` to animate the bar_rect.
    `bar_rect` is a part of the class as a property, so pass the `self` to the QPropertyAnimation.
    Notice that override the `paintEvent` method to draw the bar_rect.
    """
    def __init__(self):
        super().__init__()
        self.bar_rect = QRect(10, 10, 10, 50)  # 初始位置和大小
        self.initUI()


    def initUI(self):
        self.setWindowTitle('动画移动条')
        self.setGeometry(300, 300, 400, 200)

        # 创建动画
        self.animation = QPropertyAnimation(self, b"barGeometry")
        self.animation.setDuration(1000)  # 动画持续时间(毫秒)
        self.animation.setStartValue(QRect(10, 10, 10, 50))
        self.animation.setEndValue(QRect(100, 10, 100, 50))
        self.animation.setLoopCount(-1)  # 无限循环
        self.animation.start()


    def getBarGeometry(self):
        return self.bar_rect


    def setBarGeometry(self, rect):
        self.bar_rect = rect
        self.update()


    barGeometry = pyqtProperty(QRect, getBarGeometry, setBarGeometry)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 设置线条宽度，使其看起来更明显
        pen = QPen(QColor(0, 120, 215))
        pen.setWidth(5)  # 增加线条宽度，使其更易于看见
        painter.setPen(pen)

        # 绘制线条
        painter.drawRect(self.bar_rect)

        # 绘制文字
        painter.drawText(self.rect(), Qt.AlignCenter, "移动动画示例")


class ProgressBar(QWidget):
    """
    `geometry` is a property of QWidget, so pass the name of the property to the QPropertyAnimation constructor.
    Notice that the type of the property is QRect, so the start and end values must be QRect objects.
    """
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 400, 300)
        self.setWindowTitle("AnimationTest2")
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.frame = QFrame(self)
        # self.frame.setFixedSize(20, 50)
        self.frame.setStyleSheet("background-color: lightgray;")
        self.frame.setFrameShape(QFrame.Box)  # 设置为Box形状
        self.layout.addWidget(self.frame)
        self.setLayout(self.layout)

        # 创建动画
        self.animation = QPropertyAnimation(self.frame, b"geometry")
        self.animation.setDuration(1000)  # 动画持续时间(毫秒)
        self.animation.setStartValue(QRect(10, 10, 10, 50))
        self.animation.setEndValue(QRect(10, 10, 500, 50))
        self.animation.setLoopCount(-1)  # 无限循环
        self.animation.start()


app = QApplication([])
window = ProgressBar()
window.show()
app.exec_()
