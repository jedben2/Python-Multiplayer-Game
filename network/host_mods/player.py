from ursina import *


class Player(Entity):
    def __init__(self, position, conn, addr):
        super().__init__()
        self.hp = 100
        self.dmg = 0

        self.direction = "right"
        self.position = position
        self.dx = self.dy = 0
        self.dt = 1 / 60
        self.g = 9.8
        self.on_floor = True
        self.held_keys = []

        self.frame = 0

        self.conn = conn
        self.addr = addr

    def move(self):
        print(held_keys['d'])
        self.direction = "right"
        self.dx = held_keys['d'] * 15 * self.dt - held_keys['a'] * 15 * self.dt
        if self.dx < 0:
            self.direction = "left"
        self.frame += 1

        self.dy -= self.g * self.dt
        if self.on_floor:
            self.position[1] = 0
            self.dy = .75 * held_keys['w']
        if self.position[1] < -10:
            self.position = (0, 1)
            self.dy = 0

        self.position += (self.dx, self.dy)