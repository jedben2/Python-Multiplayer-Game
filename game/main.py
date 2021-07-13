import ursina
from player import *

app = Ursina()

window.vsync = 60
window.title = 'Multiplayer Game'
window.borderless = False
window.fullscreen_size = Vec2(1920, 1080)
window.fullscreen = True
window.exit_button.visible = True
window.fps_counter.enabled = True

player = Player(position=(-5, 0), model="quad", texture="textures/char1_Right.png", collider='box', scale_x=1, scale_y=1)
floor = Entity(position=(0, -1), model="quad", scale_x=30, collider='box')
ursina.camera.position = (player.position.x, player.position.y, -40)

# collision_zone = CollisionZone(parent=player, radius=1)

ursina.camera.zoom = -30
camera.add_script(SmoothFollow(target=player, offset=[0, 0, ursina.camera.zoom], speed=4))


def update():
    player.move(floor)


app.run()
