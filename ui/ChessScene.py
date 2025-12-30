from PySide6.QtWidgets import QGraphicsScene
from ChessSquare import ChessSquare
from constants import SQUARE_SIZE


class ChessBoard(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(self, parent)
        self.squares_map = {}
        self.init_board()


    def init_board(self):
        for i in range(64):
            new_square = ChessSquare(SQUARE_SIZE, i)
            self.addItem(new_square)
            self.squares_map[i] = new_square
