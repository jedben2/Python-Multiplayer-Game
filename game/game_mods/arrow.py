import ursina.mouse
from ursina import *
import numpy as np


class Arrow_Body(Entity):
    def __init__(self, player):
        super().__init__()
        # self.position = player.position
        self.model = "quad"
        self.scale_x = .2
        self.scale_y = .07
        self.dist = np.sqrt(.5)

    def fix_position(self, player):
        mouse_x, mouse_y = ursina.mouse.x * 100000, ursina.mouse.y * 100000
        try:
            mouse_angle = np.arctan((player.y - mouse_y) / (player.x - mouse_x))
        except:
            mouse_angle = np.pi / 2
        self.position = (player.x + self.dist * np.cos(mouse_angle), player.y + self.dist * np.sin(mouse_angle))
        self.rotation_z = -1 * mouse_angle * (180 / np.pi)
        if mouse_x < player.x:
            self.position = (
                player.x + -1 * self.dist * np.cos(mouse_angle), player.y + self.dist * np.sin(-1 * mouse_angle))


class Arrow_Head(Entity):
    def __init__(self, player):
        super().__init__()
        self.model = "quad"
        self.texture = "textures//arrow_head.png"
        self.scale = (0.2, 0.2)
        self.dist = (np.sqrt(.5) + .1)

    def fix_position(self, player):
        mouse_x, mouse_y = ursina.mouse.x * 100000, ursina.mouse.y * 100000
        try:
            mouse_angle = np.arctan((player.y - mouse_y) / (player.x - mouse_x))
        except:
            mouse_angle = np.pi / 2
        self.position = (player.x + self.dist * np.cos(mouse_angle), player.y + self.dist * np.sin(mouse_angle))
        self.rotation_z = -1 * mouse_angle * (180 / np.pi) + 90
        if mouse_x < player.x:
            self.position = (
                player.x + -1 * self.dist * np.cos(mouse_angle), player.y + self.dist * np.sin(-1 * mouse_angle))
            self.rotation_z -= 180
