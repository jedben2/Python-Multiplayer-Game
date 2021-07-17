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
        self.held_keys = {'a': 0, 'd': 0, 'w': 0}

        self.frame = 0

        self.conn = conn
        self.addr = addr

    def move(self):
        self.direction = "right"
        self.dx = int(self.held_keys['d']) * 15 * self.dt - int(self.held_keys['a']) * 15 * self.dt
        if self.dx < 0:
            self.direction = "left"
        if self.dx != 0:
            self.frame += 1

        self.dy -= self.g * self.dt
        print(f"on_floor = {self.on_floor}")
        if self.on_floor:
            self.position[1] = 0
            self.dy = .75 * int(self.held_keys['w'])
            print(f"y = {self.position[1]}, dy = {self.dy}, ")

        self.position += (self.dx, self.dy)

        if self.position[1] < 0:
            self.position = (self.position[0], 0)
            self.dy = 0
