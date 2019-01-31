import random
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame


class Cube:
    def __init__(self):
        self.front = []
        self.left = []
        self.back = []
        self.right = []
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
            self.left.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.back.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.right.append(colors[x])
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
        self.left.append('green')
        self.back.append('orange')
        self.right.append('blue')
        self.up.append('black')
        self.down.append('yellow')
        for i in range(4):
            x = random.randint(-1, ind)
            self.front.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.left.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.back.append(colors[x])
            del colors[x]
            ind -= 1
            x = random.randint(-1, ind)
            self.right.append(colors[x])
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
        self.front = []
        self.left = []
        self.back = []
        self.right = []
        self.up = []
        self.down = []

    def spin_right(self):
        self.front[:], self.left[:], self.back[:], self.right[:] = self.left[:], self.back[:], self.right[:], \
                                                                   self.front[:]
        self.up[0], self.up[1], self.up[2], self.up[5], self.up[8], self.up[7], self.up[6], \
        self.up[3] = self.up[2], self.up[5], self.up[8], self.up[7], self.up[6], self.up[3], \
                     self.up[0], self.up[1]
        self.down[0], self.down[1], self.down[2], self.down[5], self.down[8], self.down[7], self.down[6], \
        self.down[3] = self.down[2], self.down[5], self.down[8], self.down[7], self.down[6], self.down[3], \
                       self.down[0], self.down[1]
        self.print_edge

    def spin_left(self):
        self.front[:], self.right[:], self.back[:], self.left[:] = self.left[:], self.front[:], self.right[:], \
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
        self.right[0], self.right[1], self.right[2], self.right[5], self.right[8], self.right[7], self.right[6], \
        self.right[3] = self.right[6], self.right[3], self.right[0], self.right[1], self.right[2], self.right[5], \
                       self.right[8], self.right[7]
        self.left[0], self.left[1], self.left[2], self.left[5], self.left[8], self.left[7], self.left[6], \
        self.left[3] = self.left[2], self.left[5], self.left[8], self.left[7], self.left[6], self.left[3], \
                     self.left[0], self.left[1]
        self.print_edge

    def spin_down(self):
        self.front [:], self.up[:], self.back[:], self.down[:] = self.up[:], self.back[::-1], self.down[::-1], \
                                                                 self.front[6:] + self.front[3:6] + self.front[:3]
        self.left[0], self.left[1], self.left[2], self.left[5], self.left[8], self.left[7], self.left[6], \
        self.left[3] = self.left[6], self.left[3], self.left[0], self.left[1], self.left[2], self.left[5], \
                        self.left[8], self.left[7]
        self.right[0], self.right[1], self.right[2], self.right[5], self.right[8], self.right[7], self.right[6], \
        self.right[3] = self.right[2], self.right[5], self.right[8], self.right[7], self.right[6], self.right[3], \
                       self.right[0], self.right[1]
        self.print_edge

    def spin_c_u_u(self):
        self.front[7], self.front[4], self.front[1], self.up[7], self.up[4],self.up[1], self.back[1], self.back[4], \
        self.back[7], self.down[1], self.down[4], self.down[7] = self.down[1], self.down[4], self.down[7], \
                                                                 self.front[7], self.front[4], self.front[1], \
                                                                 self.up[7], self.up[4],self.up[1], self.back[1], \
                                                                 self.back[4], self.back[7]
        self.print_edge

    def spin_c_r_r(self):
        self.front[3:6], self.right[3:6], self.back[3:6], self.left[3:6] = self.left[3:6],  self.front[3:6], \
                                                                           self.right[3:6], self.back[3:6]
        self.print_edge

    def spin_c_d_d(self):
        self.front[1], self.front[4], self.front[7], self.down[7], self.down[4], self.down[1], self.back[7], \
        self.back[4], self.back[1], self.up[1], self.up[4], self.up[7] = self.up[1], self.up[4], self.up[7], \
                                                                         self.front[1], self.front[4], self.front[7], \
                                                                         self.down[7], self.down[4], self.down[1], \
                                                                         self.back[7], self.back[4], self.back[1]
        self.print_edge

    def spin_c_l_l(self):
        self.front[3:6], self.right[3:6], self.back[3:6], self.left[3:6] = self.right[3:6], self.back[3:6], \
                                                                           self.left[3:6], self.front[3:6]
        self.print_edge

    def spin_l_u_l(self):
        self.front[:4], self.right[:4], self.back[:4], self.left[:4] = self.right[:4], self.back[:4], self.left[:4], \
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
        self.front[6:], self.right[6:], self.back[6:], self.left[6:] = self.right[6:], self.back[6:], self.left[6:], \
                                                                      self.front[6:]
        self.down[0], self.down[1], self.down[2], self.down[5], self.down[8], self.down[7], self.down[6], \
        self.down[5] = self.down[6], self.down[3], self.down[0], self.down[1], self.down[2], self.down[5], \
                       self.down[8], self.down[7]
        self.print_edge

    def spin_r_u_r(self):
        self.front[:4], self.left[:4], self.back[:4], self.right[:4] = self.left[:4], self.back[:4], self.right[:4], \
                                                                       self.front[:4]
        self.up[0], self.up[1], self.up[2], self.up[5], self.up[8], self.up[7], self.up[6], \
        self.up[3] = self.up[2], self.up[5], self.up[8], self.up[7], self.up[6], self.up[3], \
                     self.up[0], self.up[1]
        self.print_edge

    def spin_r_d_r(self):
        self.front[6:], self.left[6:], self.back[6:], self.right[6:] = self.left[6:], self.back[6:], self.right[6:], \
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
        self.left[0], self.left[1], self.left[2], self.left[5], self.left[8], self.left[7], self.left[6], \
        self.left[3] = self.left[2], self.left[5], self.left[8], self.left[7], self.left[6], self.left[3], \
                       self.left[0], self.left[1]
        self.print_edge

    def spin_l_d_d(self):
        self.front[0], self.front[3], self.fron[6], self.up[0], self.up[3], self.up[6], self.back[8], self.back[5], \
        self.back[2], self.down[6], self.down[3], self.down[0] = self.up[0], self.up[3], self.up[6], self.back[8], \
                                                                 self.back[5], self.back[2], self.down[6], \
                                                                 self.down[3], self.down[0], self.front[0], \
                                                                 self.front[3], self.fron[6]
        self.left[0], self.left[1], self.left[2], self.left[5], self.left[8], self.left[7], self.left[6], \
        self.left[3] = self.left[6], self.left[3], self.left[0], self.left[1], self.left[2], self.left[5], \
                       self.left[8], self.left[7]
        self.print_edge

    def spin_r_u_u(self):
        self.front[2], self.front[5], self.front[8], self.up[2], self.up[5], self.up[8], self.back[6], self.back[3], \
        self.back[0], self.down[8], self.down[5], self.down[2] = self.down[8], self.down[5], self.down[2], \
                                                                 self.front[2], self.front[5], self.front[8], \
                                                                 self.up[2], self.up[5], self.up[8], self.back[6], \
                                                                 self.back[3], self.back[0]
        self.right[0], self.right[1], self.right[2], self.right[5], self.right[8], self.right[7], self.right[6], \
        self.right[3] = self.right[6], self.right[3], self.right[0], self.right[1], self.right[2], self.right[5], \
                        self.right[8], self.right[7]
        self.print_edge

    def spin_r_d_d(self):
        self.front[2], self.front[5], self.front[8], self.up[2], self.up[5], self.up[8], self.back[6], self.back[3], \
        self.back[0], self.down[8], self.down[5], self.down[2] = self.up[2], self.up[5], self.up[8], self.back[6], \
                                                                 self.back[3], self.back[0], self.down[8], \
                                                                 self.down[5], self.down[2], self.front[2], \
                                                                 self.front[5], self.front[8]
        self.right[0], self.right[1], self.right[2], self.right[5], self.right[8], self.right[7], self.right[6], \
        self.right[3] = self.right[2], self.right[5], self.right[8], self.right[7], self.right[6], self.right[3], \
                        self.right[0], self.right[1]
        self.print_edge

    def print_edge(self):
        self.l_left_up.setText(self.front[0])
        self.l_center_up.setText(self.front[1])
        self.l_right_up.setText(self.front[2])
        self.l_leftcenter.setText(self.front[3])
        self.l_center.setText(self.front[4])
        self.l_right_centersetText(self.front[5])
        self.l_left_down.setText(self.front[6])
        self.l_center_down.setText(self.front[7])
        self.l_right_down.setText(self.front[8])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cube()
    ex.show()
    sys.exit(app.exec())