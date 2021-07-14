from ursina import *


class Player(Entity):
    def __init__(self, position, model, texture, collider, scale_x, scale_y, char_num):
        super().__init__()
        self.hp = 100
        self.dmg = 0
        self.char_num = char_num

        self.position = position
        self.dx = self.dy = 0
        self.dt = 1 / 60
        self.g = 9.8

        self.model = model
        self.texture = texture
        self.collider = collider
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.always_on_top = True

        self.frame = 0

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.hp -= self.dmg

    def attack(self, other):
        pass

    def is_hit(self):
        pass

    def move(self, other):
        if self.char_num == "1":
            self.dx = held_keys['d'] * 15 * self.dt - held_keys['a'] * 15 * self.dt
        else:
            self.dx = held_keys['right arrow'] * 15 * self.dt - held_keys['left arrow'] * 15 * self.dt
        if self.dx < 0:
            if self.frame > 9:
                self.frame = 0
            if self.frame % 3 == 0:
                self.texture = f"animations//char{self.char_num}_walk_left//{self.frame // 3}.png"
        elif self.dx > 0:
            if self.frame > 9:
                self.frame = 0
            if self.frame % 3 == 0:
                self.texture = f"animations//char{self.char_num}_walk_right//{self.frame // 3}.png"
        self.frame += 1

        self.dy -= self.g * self.dt
        if self.intersects(other).hit:
            self.y = 0
            if self.char_num == "1":
                self.dy = .75 * held_keys['w']
            else:
                self.dy = .75 * held_keys['up arrow']
        if self.y < -10:
            self.y = 1
            self.x = 0
            self.dy = 0
