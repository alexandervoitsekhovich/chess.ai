from PySide6 import QtCore, QtWidgets, QtGui
import sys


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hello = "Hello, chess.ai"
        self.button = QtWidgets.QPushButton("Let`s start!")
        self.text = QtWidgets.QLabel("Hello, chess.ai", alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)


    @QtCore.Slot()
    def magic(self):
        self.text.setText(self.hello)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Widget()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
