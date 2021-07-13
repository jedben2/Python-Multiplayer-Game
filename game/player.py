from ursina import *


class Player(Entity):
    def __init__(self, position, model, texture, collider):
        super().__init__()
        self.hp = 100
        self.dmg = 0

        self.position = position
        self.dx = self.dy = 0
        self.dt = 1 / 60
        self.g = 9.8

        self.model = model
        self.texture = texture
        self.collider = collider

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.hp -= self.dmg

    def attack(self, other):
        pass

    def move(self):
        self.dx = 0
        self.dy -= self.g * self.dt
        self.dx += held_keys['d'] * 15 * self.dt - held_keys['a'] * 15 * self.dt

    def check_collide(self, other):
        self.y -= .5
        if self.intersects(other).hit:
            self.dy = 0
        self.y += .5
        return
