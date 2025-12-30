from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPen


class ChessSquare(QGraphicsRectItem):
    def __init__(self, SQUARE_SIZE, i):
        super().__init__(0, 0, SQUARE_SIZE, SQUARE_SIZE)
        self.setPos(SQUARE_SIZE * (i % 8), SQUARE_SIZE * (7 - i // 8))
        self.setPen(Qt.PenStyle.NoPen)
        if (SQUARE_SIZE * (i % 8) + SQUARE_SIZE * (7 - i // 8)) % 2 == 0:
            self.setBrush(QBrush((118, 150, 86)))
        else:
            self.setBrush(QBrush((179, 203, 155)))
