from ChessView import ChessView
from ChessBoard import ChessBoard
from PySide6.QtWidgets import QMainWindow
from constants import SQUARE_SIZE

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chess.ai")
        self.scene = ChessBoard()
        self.view = ChessView(self.scene)
        self.setCentralWidget(self.view)
        self.width_margin, self.height_margin = 150, 50
        self.view.setFixedSize(SQUARE_SIZE * 8 + self.width_margin * 2, SQUARE_SIZE * 8 + self.height_margin * 2)
        self.adjustSize()
        