from ursina import *


class Player(Entity):
    def __init__(self, position, model, texture, collider, scale_x, scale_y, char_num):
        super().__init__()
        self.hp = 100
        self.char_num = char_num

        self.position = position

        self.direction = "right"
        self.model = model
        self.texture = texture
        self.collider = collider
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.always_on_top = True

        self.frame = 0

    def flip(self):
        if self.frame > 9:
            self.frame = 0
        if self.direction == "left":
            if self.frame % 3 == 0:
                self.texture = f"animations//char1_walk_left//{self.frame // 3}.png"
        else:
            if self.frame % 3 == 0:
                self.texture = f"animations//char1_walk_right//{self.frame // 3}.png"
