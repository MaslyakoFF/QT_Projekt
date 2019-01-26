import random


class Edge:
    def __init__(self):
        colors = ['red', 'green', 'orange', 'blue', 'black', 'yellow', 'red',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow',
                  'red', 'green', 'orange', 'blue', 'black', 'yellow', ]
        self.front = []
        self.left = []
        self.back = []
        self.right = []
        self.up = []
        self.down = []
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