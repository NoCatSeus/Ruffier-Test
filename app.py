from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
)

from instr import *
from test import TestWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.init_UI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


    def init_UI(self):
        self.text_title = QLabel(txt_hello)
        self.text_instruction = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.text_title, alignment = Qt.AlignmentFlag.AlignLeft)
        self.main_layout.addWidget(self.text_instruction, alignment = Qt.AlignmentFlag.AlignLeft)
        self.main_layout.addWidget(self.btn_next, alignment = Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.main_layout)

    def connects(self):
        self.btn_next.clicked.connect(self.next_screen)

    def next_screen(self):
        self.next_win = TestWindow()
        self.hide()

app = QApplication([])
window = MainWindow()
app.exec_()