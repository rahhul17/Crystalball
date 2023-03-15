import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import QTimer, Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        hbox = QHBoxLayout(self)

        self.button = QPushButton('Press me', self)
        self.button.clicked.connect(self.show_text)

        hbox.addWidget(self.button, alignment=Qt.AlignCenter)

        self.label = QLabel(self)
        self.label.setVisible(False)

        self.timer = QTimer()
        self.timer.timeout.connect(self.hide_text)

        self.setLayout(hbox)

    def show_text(self):
        self.label.setText('Hello')
        self.label.move(self.button.x(), self.button.y() + self.button.height() + 5)
        self.label.setVisible(True)
        self.timer.start(3000)

    def hide_text(self):
        self.label.setVisible(False)
        self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(300, 200)
    widget.show()
    sys.exit(app.exec())