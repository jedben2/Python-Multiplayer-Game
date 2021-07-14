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

