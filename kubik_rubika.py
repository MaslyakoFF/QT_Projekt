import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame
from PyQt5.QtGui import QPainter, QColor


class Cube:
    def __init__(self):
        self.front = []
        self.left1 = []
        self.back = []
        self.right1 = []
        self.up = []
        self.down = []

    def start(self):
        colors = ['red', 'green', 'orange', 'blue', 'black', 'yellow', 'red',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow', ]
        ind = 47
        for i in range(4):
            x = random.randint(-1, ind)
            self.front.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.left1.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.back.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.right1.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.up.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.down.append(colors[x])
            del colors[x]
            ind -= 1
        self.front.append('red')
        self.left1.append('green')
        self.back.append('orange')
        self.right1.append('blue')
        self.up.append('black')
        self.down.append('yellow')
        for i in range(4):
            x = random.randint(-1, ind)
            self.front.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.left1.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.back.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.right1.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.up.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.down.append(colors[x])
            del colors[x]
            ind -= 1


class Operations(QMainWindow, QFrame, Cube):
    def __init__(self):
        super().__init__()
        uic.loadUi('window.ui', self)
        self.start()

    def initUI(self):
        self.l_u_u.clicked.connect(self.spin_l_u_u)
        self.c_u_u.clicked.connect(self.spin_c_u_u)
        self.r_u_u.clicked.connect(self.spin_r_u_u)
        self.r_u_r.clicked.connect(self.spin_r_u_r)
        self.c_r_r.clicked.connect(self.spin_c_r_r)
        self.r_d_r.clicked.connect(self.spin_r_d_r)
        self.r_d_d.clicked.connect(self.spin_r_d_d)
        self.c_d_d.clicked.connect(self.spin_c_d_d)
        self.l_d_d.clicked.connect(self.spin_l_d_d)
        self.l_d_l.clicked.connect(self.spin_l_d_l)
        self.c_l_l.clicked.connect(self.spin_c_l_l)
        self.l_u_l.clicked.connect(self.spin_l_u_l)
        self.spinLeft.clicked.connect(self.spin_left)
        self.spinDown.clicked.connect(self.spin_down)
        self.spinRight.clicked.connect(self.spin_right)
        self.spinUp.clicked.connect(self.spin_up)
        self.restart.clicked.connect(self.start)

        self.show()

    def spin_right(self):
        self.front[:], self.left1[:], self.back[:], self.right1[:] = self.left1[:], self.back[:], self.right1[:], \
                                                                   self.front[:]
        self.up[0], self.up[1], self.up[2], self.up[5], self.up[8], self.up[7], self.up[6], \
        self.up[3] = self.up[2], self.up[5], self.up[8], self.up[7], self.up[6], self.up[3], \
                     self.up[0], self.up[1]
        self.down[0], self.down[1], self.down[2], self.down[5], self.down[8], self.down[7], self.down[6], \
        self.down[3] = self.down[2], self.down[5], self.down[8], self.down[7], self.down[6], self.down[3], \
                       self.down[0], self.down[1]
        self.paintEvent

    def spin_left(self):
        self.front[:], self.right1[:], self.back[:], self.left1[:] = self.left1[:], self.front[:], self.right1[:], \
                                                                   self.back[:]
        self.up[0], self.up[1], self.up[2], self.up[5], self.up[8], self.up[7], self.up[6], self.up[3] = self.up[6], \
                                                                                                         self.up[3], \
                                                                                                         self.up[0], \
                                                                                                         self.up[1], \
                                                                                                         self.up[2], \
                                                                                                         self.up[5], \
                                                                                                         self.up[8], \
                                                                                                         self.up[7]
        self.down[0], self.down[1], self.down[2], self.down[5],self.down[8], self.down[7], self.down[6], \
        self.down[5] = self.down[6], self.down[3], self.down[0], self.down[1], self.down[2], self.down[5], \
                       self.down[8], self.down[7]
        self.print_edge

    def spin_up(self):
        self.front[:], self.up[:], self.back[:], self.down[:] = self.down[6:] + self.down[3:6] + self.down[:3], \
                                                                self.front[:], self.up[::-1], self.back[::-1]
        self.right1[0], self.right1[1], self.right1[2], self.right1[5], self.right1[8], self.right1[7], self.right1[6], \
        self.right1[3] = self.right1[6], self.right1[3], self.right1[0], self.right1[1], self.right1[2], self.right1[5], \
                       self.right1[8], self.right1[7]
        self.left1[0], self.left1[1], self.left1[2], self.left1[5], self.left1[8], self.left1[7], self.left1[6], \
        self.left1[3] = self.left1[2], self.left1[5], self.left1[8], self.left1[7], self.left1[6], self.left1[3], \
                     self.left1[0], self.left1[1]
        self.print_edge

    def spin_down(self):
        self.front [:], self.up[:], self.back[:], self.down[:] = self.up[:], self.back[::-1], self.down[::-1], \
                                                                 self.front[6:] + self.front[3:6] + self.front[:3]
        self.left1[0], self.left1[1], self.left1[2], self.left1[5], self.left1[8], self.left1[7], self.left1[6], \
        self.left1[3] = self.left1[6], self.left1[3], self.left1[0], self.left1[1], self.left1[2], self.left1[5], \
                        self.left1[8], self.left1[7]
        self.right1[0], self.right1[1], self.right1[2], self.right1[5], self.right1[8], self.right1[7], self.right1[6], \
        self.right1[3] = self.right1[2], self.right1[5], self.right1[8], self.right1[7], self.right1[6], self.right1[3], \
                       self.right1[0], self.right1[1]
        self.print_edge

    def spin_c_u_u(self):
        self.front[7], self.front[4], self.front[1], self.up[7], self.up[4],self.up[1], self.back[1], self.back[4], \
        self.back[7], self.down[1], self.down[4], self.down[7] = self.down[1], self.down[4], self.down[7], \
                                                                 self.front[7], self.front[4], self.front[1], \
                                                                 self.up[7], self.up[4],self.up[1], self.back[1], \
                                                                 self.back[4], self.back[7]
        self.print_edge

    def spin_c_r_r(self):
        self.front[3:6], self.right1[3:6], self.back[3:6], self.left1[3:6] = self.left1[3:6],  self.front[3:6], \
                                                                           self.right1[3:6], self.back[3:6]
        self.print_edge

    def spin_c_d_d(self):
        self.front[1], self.front[4], self.front[7], self.down[7], self.down[4], self.down[1], self.back[7], \
        self.back[4], self.back[1], self.up[1], self.up[4], self.up[7] = self.up[1], self.up[4], self.up[7], \
                                                                         self.front[1], self.front[4], self.front[7], \
                                                                         self.down[7], self.down[4], self.down[1], \
                                                                         self.back[7], self.back[4], self.back[1]
        self.print_edge

    def spin_c_l_l(self):
        self.front[3:6], self.right1[3:6], self.back[3:6], self.left1[3:6] = self.right1[3:6], self.back[3:6], \
                                                                           self.left1[3:6], self.front[3:6]
        self.print_edge

    def spin_l_u_l(self):
        self.front[:4], self.right1[:4], self.back[:4], self.left1[:4] = self.right1[:4], self.back[:4], self.left1[:4], \
                                                                       self.front[:4]
        self.up[0], self.up[1], self.up[2], self.up[5], self.up[8], self.up[7], self.up[6], self.up[3] = self.up[6], \
                                                                                                         self.up[3], \
                                                                                                         self.up[0], \
                                                                                                         self.up[1], \
                                                                                                         self.up[2], \
                                                                                                         self.up[5], \
                                                                                                         self.up[8], \
                                                                                                         self.up[7]
        self.print_edge

    def spin_l_d_l(self):
        self.front[6:], self.right1[6:], self.back[6:], self.left1[6:] = self.right1[6:], self.back[6:], self.left1[6:], \
                                                                      self.front[6:]
        self.down[0], self.down[1], self.down[2], self.down[5], self.down[8], self.down[7], self.down[6], \
        self.down[5] = self.down[6], self.down[3], self.down[0], self.down[1], self.down[2], self.down[5], \
                       self.down[8], self.down[7]
        self.print_edge

    def spin_r_u_r(self):
        self.front[:4], self.left1[:4], self.back[:4], self.right1[:4] = self.left1[:4], self.back[:4], self.right1[:4], \
                                                                       self.front[:4]
        self.up[0], self.up[1], self.up[2], self.up[5], self.up[8], self.up[7], self.up[6], \
        self.up[3] = self.up[2], self.up[5], self.up[8], self.up[7], self.up[6], self.up[3], \
                     self.up[0], self.up[1]
        self.print_edge

    def spin_r_d_r(self):
        self.front[6:], self.left1[6:], self.back[6:], self.right1[6:] = self.left1[6:], self.back[6:], self.right1[6:], \
                                                                       self.front[6:]
        self.down[0], self.down[1], self.down[2], self.down[5], self.down[8], self.down[7], self.down[6], \
        self.down[3] = self.down[2], self.down[5], self.down[8], self.down[7], self.down[6], self.down[3], \
                       self.down[0], self.down[1]
        self.print_edge

    def spin_l_u_u(self):
        self.front[0], self.front[3], self.fron[6], self.up[0], self.up[3], self.up[6], self.back[8], self.back[5], \
        self.back[2], self.down[6], self.down[3], self.down[0] = self.down[6], self.down[3], self.down[0], \
                                                                 self.front[0], self.front[3], self.fron[6], \
                                                                 self.up[0], self.up[3], self.up[6], self.back[8], \
                                                                 self.back[5], self.back[2]
        self.left1[0], self.left1[1], self.left1[2], self.left1[5], self.left1[8], self.left1[7], self.left1[6], \
        self.left1[3] = self.left1[2], self.left1[5], self.left1[8], self.left1[7], self.left1[6], self.left1[3], \
                       self.left1[0], self.left1[1]
        self.print_edge

    def spin_l_d_d(self):
        self.front[0], self.front[3], self.fron[6], self.up[0], self.up[3], self.up[6], self.back[8], self.back[5], \
        self.back[2], self.down[6], self.down[3], self.down[0] = self.up[0], self.up[3], self.up[6], self.back[8], \
                                                                 self.back[5], self.back[2], self.down[6], \
                                                                 self.down[3], self.down[0], self.front[0], \
                                                                 self.front[3], self.fron[6]
        self.left1[0], self.left1[1], self.left1[2], self.left1[5], self.left1[8], self.left1[7], self.left1[6], \
        self.left1[3] = self.left1[6], self.left1[3], self.left1[0], self.left1[1], self.left1[2], self.left1[5], \
                       self.left1[8], self.left1[7]
        self.print_edge

    def spin_r_u_u(self):
        self.front[2], self.front[5], self.front[8], self.up[2], self.up[5], self.up[8], self.back[6], self.back[3], \
        self.back[0], self.down[8], self.down[5], self.down[2] = self.down[8], self.down[5], self.down[2], \
                                                                 self.front[2], self.front[5], self.front[8], \
                                                                 self.up[2], self.up[5], self.up[8], self.back[6], \
                                                                 self.back[3], self.back[0]
        self.right1[0], self.right1[1], self.right1[2], self.right1[5], self.right1[8], self.right1[7], self.right1[6], \
        self.right1[3] = self.right1[6], self.right1[3], self.right1[0], self.right1[1], self.right1[2], self.right1[5], \
                        self.right1[8], self.right1[7]
        self.print_edge

    def spin_r_d_d(self):
        self.front[2], self.front[5], self.front[8], self.up[2], self.up[5], self.up[8], self.back[6], self.back[3], \
        self.back[0], self.down[8], self.down[5], self.down[2] = self.up[2], self.up[5], self.up[8], self.back[6], \
                                                                 self.back[3], self.back[0], self.down[8], \
                                                                 self.down[5], self.down[2], self.front[2], \
                                                                 self.front[5], self.front[8]
        self.right1[0], self.right1[1], self.right1[2], self.right1[5], self.right1[8], self.right1[7], self.right1[6], \
        self.right1[3] = self.right1[2], self.right1[5], self.right1[8], self.right1[7], self.right1[6], self.right1[3], \
                        self.right1[0], self.right1[1]
        self.print_edge

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.print_edge(qp)
        qp.end()

    def print_edge(self, qp):
        qp.setBrush(QColor(self.front[0]))
        qp.drawRect(50, 50, 50, 50)
        qp.setBrush(QColor(self.front[1]))
        qp.drawRect(100, 50, 50, 50)
        qp.setBrush(QColor(self.front[2]))
        qp.drawRect(150, 50, 50, 50)
        qp.setBrush(QColor(self.front[3]))
        qp.drawRect(50, 100, 50, 50)
        qp.setBrush(QColor(self.front[4]))
        qp.drawRect(100, 100, 50, 50)
        qp.setBrush(QColor(self.front[5]))
        qp.drawRect(150, 100, 50, 50)
        qp.setBrush(QColor(self.front[6]))
        qp.drawRect(50, 150, 50, 50)
        qp.setBrush(QColor(self.front[7]))
        qp.drawRect(100, 150, 50, 50)
        qp.setBrush(QColor(self.front[8]))
        qp.drawRect(150, 150, 50, 50)


app = QApplication(sys.argv)
ex = Operations()
ex.show()
sys.exit(app.exec_())