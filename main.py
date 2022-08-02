from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QBrush, QPen
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QPoint
import sys
import random
import numpy as np

list = [0, 1, 2, 3]

output = random.choices(list, weights=[10, 50, 5, 35], k = 20)
print(output)

edgesList = [(1, 2), (1, 5), (1, 6),
                 (2, 1), (2, 3), (2, 5), (2, 6), (2, 7),
                 (3, 2), (3, 4), (3, 6), (3, 7), (3, 8),
                 (4, 3), (4, 7), (4, 8),
                 (5, 1), (5, 2), (5, 6), (5, 9), (5, 10),
                 (6, 1), (6, 2), (6, 3), (6, 5), (6, 7), (6, 9), (6, 10), (6, 11),
                 (7, 2), (7, 3), (7, 4), (7, 6), (7, 8), (7, 10), (7, 11), (7, 12),
                 (8, 3), (8, 4), (8, 7), (8, 11), (8, 12),
                 (9, 5), (9, 6), (9, 10), (9, 14), (9, 13),
                 (10, 5), (10, 6), (10, 7), (10, 9), (10, 11), (10, 13), (10, 14), (10, 15),
                 (11, 6), (11, 7), (11, 8), (11, 10), (11, 12), (11, 14), (11, 15), (11, 16),
                 (12, 7), (12, 8), (12, 11), (12, 15), (12, 16),
                 (13, 9), (13, 10), (13, 14),
                 (14, 9), (14, 10), (14, 11), (14, 13), (14, 15),
                 (15, 10), (15, 11), (15, 12), (15, 14), (15, 16),
                 (16, 11), (16, 12), (16, 15)
                 ]

edgesList2 = [(1, 2), (1, 5), (1, 6),
                 (2, 1), (2, 3), (2, 5), (2, 6), (2, 7),
                 (3, 2), (3, 4), (3, 6), (3, 7), (3, 8),
                 (4, 3), (4, 7), (4, 8),
                 (5, 1), (5, 2), (5, 6), (5, 9), (5, 10)]

connectionsList = [(0, 3, 0.6), (0 , 4, 0.4), (3, 0, 0.3), (3, 8, 0.7), (4, 0, 0.2), (4, 8, 0.4), (4, 9, 0.4),
                    (8, 3, 0.1), (8, 4, 0.3), (8, 13, 0.6), (9, 4, 0.3), (9, 13, 0.2), (9, 5, 0.5),
                     (13, 8, 0.3), (13, 9, 0.3), (13, 17, 0.4), (17, 13, 0.5), (17, 16, 0.), (16, 17, 1),
                     (5, 1, 0.3), (5, 6, 0.5), (5, 9, 0.2), (1, 2, 0.5), (1, 5, 0.5),
                     (2, 1, 0.5), (2, 6, 0.5), (6, 2, 0.1), (6, 5, 0.2), (6, 7, 0.2), (6, 10, 0.5),
                     (7, 6, 0.2), (7, 11, 0.4), (7, 12, 0.4), (10, 5, 0.2), (10, 6, 0.2),
                     (10, 11, 0.2), (10, 14, 0.4), (11, 7, 0.2), (11, 10, 0.2), (11, 12, 0.3),
                     (11, 14, 0.3), (12, 7, 0.2), (12, 11, 0.2), (12, 15, 0.6), (14, 10, 0.2),
                     (14, 11, 0.2), (14, 15, 0.2), (14, 18, 0.4), (18, 14, 1), (15, 12, 0.2),
                     (15, 14, 0.2), (15, 19, 0.6), (19, 15, 1)]

edgesCoords = [(0, 118, 114), (1, 138, 114),  (2, 118, 200), (3, 138, 200), (4, 198, 114),
                (5, 218, 114), (6, 198, 200), (7, 218, 200), (8, 400, 114), (9, 420, 114), 
                (10, 354, 200), (11, 374, 200), (12, 282, 200), (13, 302, 200), (14, 198, 274),
                (15, 218, 274), (16, 282, 274), (17, 302, 274), (18, 374, 200), (19, 198, 352),
                (20, 218, 352), (21, 128, 386), (22, 128, 406), (23, 76, 436), (24, 96, 436),
                (25, 128, 466), (26, 128, 486), (27, 154, 436), (28, 174, 436), (29, 194, 436),
                (30, 214, 436), (31, 206, 466), (32, 206, 486), (33, 154, 512), (34, 174, 512),
                (35, 206, 544), (36, 206, 564), (37, 206, 586), (38, 206, 606), (39, 234, 512),
                (40, 254, 512), (41, 234, 592), (42, 254, 592), (43, 274, 512), (44, 294, 512),
                (45, 284, 544), (46, 284, 564), (47, 314, 592), (48, 334, 592), (49, 284, 624),
                (50, 284, 644), (51, 358, 512), (52, 378, 512), (53, 358, 678), (54, 378, 678)]

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.child = QWidget(self)
        for x in edgesCoords:
            tt = QLabel(str(x[0]), self)
            tt.move(x[1], x[2])
        self.child.setStyleSheet("background-color:blue;border-radius:15px;")
        self.child.resize(10, 10)
        self.top= 150
        self.left= 150
        self.width = 500
        self.height = 800
        self.radius = 80
        
        self.InitWindow()

    def InitWindow(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
        self.anim_group = QSequentialAnimationGroup()
        self.starting_point = 0
        self.ending_point = self.chooseNextPoint(self.starting_point)
        while True:
            if self.ending_point == 19:
                self.anim_group.addAnimation(self.animate(self.starting_point, self.ending_point))
                break
            else:
                self.anim_group.addAnimation(self.animate(self.starting_point, self.ending_point))
                self.starting_point = self.ending_point
                self.ending_point = self.chooseNextPoint(self.starting_point)
        #self.animate(self.starting_point, self.ending_point)
        self.anim_group.start()
        self.starting_point = self.ending_point
        self.ending_point = self.chooseNextPoint(self.starting_point)
        print(f'{self.starting_point}, ccc')
        #self.animate(self.starting_point, self.ending_point)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen())
        painter.setPen(Qt.GlobalColor.black)
        #painter.drawEllipse(40, 40, 400, 400)
        for edge in edgesList2:
            painter.drawEllipse(edge[0]*self.radius, edge[1]*self.radius, 20, 20)
        for conn in connectionsList:
            #print(edgesList[conn[0]][0])
            dir_angle_x = edgesList2[conn[1]][0] - edgesList2[conn[0]][0]
            dir_angle_y = edgesList[conn[1]][1] - edgesList[conn[0]][1]
            sinu = dir_angle_x/(dir_angle_x**2+dir_angle_y**2)
            degg_sin = np.arcsin(sinu)
            painter.drawLine(edgesList2[conn[0]][0]*self.radius + 10, edgesList2[conn[0]][1]*self.radius + 10, edgesList[conn[1]][0]*self.radius + 10, edgesList[conn[1]][1]*self.radius + 10)
        painter.drawLine(20, 20, 10, 10)

    def animate(self, ind0, ind1):
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setStartValue(QPoint(edgesList[ind0][0]*80, edgesList[ind0][1]*80))
        self.anim.setEndValue(QPoint(edgesList[ind1][0]*80, edgesList[ind1][1]*80))
        self.anim.setDuration(300)
        return self.anim
        #self.anim.start()

    def chooseNextPoint(self, point):
        conn2 = filter(lambda x: x[0] == point, connectionsList)
        out_points_possibles = []
        probabilities = []
        for i in conn2:
            out_points_possibles.append(i[1])
            probabilities.append(i[2])
        print(out_points_possibles)
        print(probabilities)
        output = random.choices(out_points_possibles, weights=probabilities, k = 1)
        print(output[0])
        return output[0]
        


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())