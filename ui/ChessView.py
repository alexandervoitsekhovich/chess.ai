from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QBrush, QPainter
from PySide6.QtCore import Qt



class ChessView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(self)
        self.setBackgroundBrush(QBrush((19, 20, 22)))
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
