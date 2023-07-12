import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget, QWidget,QPushButton,QFrame,QMessageBox
from PyQt5.QtCore import Qt,QSize,QCoreApplication
from PyQt5.QtGui import QIcon, QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arayüz")
        self.setFixedSize(120, 60)

        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = screen.height() - self.height() - 100
        self.move(x, y)

        self.frame = QFrame(self)
        self.frame.setGeometry(0, 0, 120, 60)
        self.frame.setStyleSheet('background-color: #222; border-radius: 15px; color: #fff;')

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setWindowOpacity(0.9)
        
        self.button = QPushButton(self)
        self.button.setIcon(QIcon("src/mic_white_48dp.png"))
        self.button.setIconSize(QSize(35, 35))
        self.button.setGeometry(0, 0, 60, 60)
        self.button.clicked.connect(openSr)
        self.button.setStyleSheet("""
                            QPushButton {
                                background: transparent; 
                                padding: 0;
                                border: none
                            }
                            QPushButton:hover {
                                background: rgba(0, 0, 0, 0.5);
                                border-top-left-radius: 15px;
                                border-bottom-left-radius: 15px;
                            }
                                """)

        self.button1 = QPushButton(self)
        self.button1.setIcon(QIcon("src/round_close_white_48dp.png"))
        self.button1.setIconSize(QSize(35, 35))
        self.button1.setGeometry(60, 0, 60, 60)
        self.button1.clicked.connect(QCoreApplication.instance().quit)
        self.button1.setStyleSheet("""
                            QPushButton {
                                background: transparent; 
                                padding: 0;
                                border: none
                            }
                            QPushButton:hover {
                                background: rgba(150, 0, 0, 0.5);
                                border-top-right-radius: 15px;
                                border-bottom-right-radius: 15px;
                            }
                                """)

import pyautogui 
def openSr():
    pyautogui.hotkey('alt', 'tab')
    os.system('python main.py')

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
