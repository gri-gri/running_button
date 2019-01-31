import sys
import os
import playsound
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from math import sqrt
from random import randint
 
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.initUI()
 
    def initUI(self):
        self.setGeometry(0, 0, 1200, 1200)
        self.setWindowTitle('Нажмите m, чтобы включить музыку')
 
        self.button = QPushButton('Подтвердить', self)
        self.button.move(100, 100)
        self.button.resize(self.button.sizeHint())

        self.show()
 
    def mouseMoveEvent(self, event):
        x1 = event.x()
        y1 = event.y()
        x = self.button.x()
        y = self.button.y()
        w = self.button.width()
        h = self.button.width()
        if sqrt(min((x1-x)**2, (x1-x-w)**2)+min((y1-y)**2, (y1-y-h)**2)) <= 50:
            x2, y2 = randint(1, self.width()), randint(1, self.height())
            while not self.isvalid([x2, y2], [x1, y1]):
                x2, y2 = randint(1, self.width()), randint(1, self.height())
            self.button.move(x2, y2)

    def isvalid(self, coors, coors_cursor):
        if 0 < coors[0] and 0 < coors[1] and\
           coors[0] + self.button.width() < self.width() \
           and coors[1] + self.button.height() < self.height() \
           and not((coors[0] <= coors_cursor[0] <= coors[0] + self.button.width())\
                   and (coors[1] <= coors_cursor[1] <= coors[1] + self.button.height())):
            return True
        return False

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_M:
            playsound.playsound('sound.mp3', block=False)
            
    ''' Вот так я пытался сделать нормально, но, к сожалению, не фурычило
    def AI_calculate_coors(self, x_button, y_button, w_button, h_button,
                           x_cursor, y_cursor, w_window, h_window):
        if x_cursor < x_button:
            if y_cursor < y_button:
                if sqrt((x_button-x_cursor)**2+(y_button-y_cursor)**2) <= DELTA:
                    if x_cursor+DELTA+OFFSET+w_button < w_window:
                        if y_cursor+DELTA+OFFSET+h_button < h_window:
                            return x_cursor+DELTA+OFFSET, y_cursor+DELTA+OFFSET
                        else:
                            return x_cursor+DELTA+OFFSET, y_cursor-DELTA-2*OFFSET
                    else:
                        if y_cursor+DELTA+OFFSET+h_button < h_window:
                            return x_cursor-DELTA-2*OFFSET, y_cursor+DELTA+OFFSET
                        else:
                            return x_cursor-DELTA-2*OFFSET, y_cursor-DELTA-2*OFFSET
            elif y_button <= y_cursor <= y_button+h_button:
                if x_button - x_cursor <= DELTA:
                    if x_cursor+DELTA+OFFSET+w_button < w_window:
                        return x_cursor+DELTA+OFFSET, y_button
                    else:
                        if y_cursor+DELTA+OFFSET+h_button < h_window:
                            return x_cursor-OFFSET, y_cursor+DELTA+OFFSET
                        else:
                            return x_cursor-OFFSET, y_cursor-DELTA-2*OFFSET
            else:
                if sqrt((x_button-x_cursor)**2+(y_cursor-(y_button+h_button)**2)) <= DELTA:
                    if x_cursor+DELTA+OFFSET+w_button < w_window:
                        if y_cursor-DELTA-OFFSET > 0:
                            return x_cursor+DELTA+OFFSET, y_cursor-DELTA-OFFSET
                        else:
                            return x_cursor+DELTA+OFFSET, y_cursor+DELTA+2*OFFSET
                    else:
                        if y_cursor+DELTA+OFFSET+h_button < h_window:
                            return x_cursor-DELTA-2*OFFSET, y_cursor-DELTA-OFFSET
                        else:
                            return x_cursor+DELTA+2*OFFSET, y_cursor+DELTA+2*OFFSET
        elif x_button <= x_cursor <= x_button+w_button:
            if y_cursor < y_button:
                if y_button - y_cursor <= DELTA:
                    if y_cursor+DELTA+OFFSET+h_button < h_window:
                        return x_button, y_cursor+DELTA+OFFSET
                    else:
                        if x_cursor-DELTA-2*OFFSET > 0:
                            return x_cursor-DELTA-2*OFFSET, y_cursor-OFFSET
                        else:
                            return x_cursor+DELTA+2*OFFSET, y_cursor-OFFSET
                        
            elif y_button <= y_cursor <= y_button+h_button:
                print('O_o')
            else:
                if y_cursor - y_button <= DELTA:
                    if y_cursor-DELTA-OFFSET > 0:
                        return x_button, y_cursor-DELTA-OFFSET
                    else:
                        if x_cursor+DELTA+OFFSET+w_button < w_window:
                            return x_cursor+DELTA+OFFSET, y_cursor+OFFSET
                        else:
                            return x_cursor-DELTA-2*OFFSET, y_cursor+OFFSET
        else:
            if y_cursor < y_button:
                if sqrt((x_cursor-(x_button+w_button))**2+(y_button-y_cursor)**2) <= DELTA:
                    if x_cursor-DELTA-OFFSET > 0:
                        if y_cursor+DELTA+OFFSET+h_button < h_window:
                            return x_cursor-DELTA-OFFSET, y_cursor+DELTA+OFFSET
                        else:
                            return x_cursor-DELTA-OFFSET, y_cursor-DELTA-2*OFFSET
                    else:
                        if y_cursor+DELTA+OFFSET+h_button < h_window:
                            return x_cursor-OFFSET, y_cursor+DELTA+2*OFFSET
                        else:
                            return x_cursor+OFFSET, y_cursor+DELTA+2*OFFSET
            elif y_button <= y_cursor <= y_button+h_button:
                if x_cursor - x_button <= DELTA:
                    if x_cursor-DELTA-OFFSET > 0:
                        return x_cursor-DELTA-OFFSET, y_button
                    else:
                        if y_cursor-DELTA-2*OFFSET > 0:
                            return x_cursor-OFFSET, y_cursor-DELTA-2*OFFSET
                        else:
                            return x_cursor-OFFSET, y_cursor+DELTA+2*OFFSET
            else:
                if sqrt((x_cursor-(x_button+w_button)**2+(y_cursor-(y_button+h_button)**2))) <= DELTA:
                    if x_cursor-DELTA-OFFSET > 0:
                        if y_cursor-DELTA-OFFSET > 0:
                            return x_cursor-DELTA-OFFSET, y_cursor-DELTA-OFFSET
                        else:
                            return x_cursor-DELTA-2*OFFSET, y_cursor+OFFSET
                    else:
                        if y_cursor-DELTA-2*OFFSET > 0:
                            return x_cursor+OFFSET, y_cursor-DELTA-2*OFFSET
                        else:
                            return x_cursor+OFFSET, y_cursor+DELTA+2*OFFSET
        return x_button, y_button
    '''
                          

DELTA = 50
OFFSET = 15
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = MyWidget()
    sys.exit(app.exec_())
