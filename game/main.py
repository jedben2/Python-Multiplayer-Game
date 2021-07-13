from player import *

app = Ursina()

window.vsync = 60
window.title = 'Multiplayer Game'
window.borderless = False
window.fullscreen = True
window.exit_button.visible = True
window.fps_counter.enabled = True

dt = 1 / window.vsync

# player = Player(0, 0, 'square')
player = Player(position=(-5, 0), model="quad", texture="brick", collider='box')
floor = Entity(position=(0, -2), model='quad', scale_x=30, collider='box')
ursina.camera.position = (player.position.x, player.position.y, -40)

collision_zone = CollisionZone(parent=player, radius=1)

ursina.camera.zoom = -40


def update():
    ursina.camera.zoom += held_keys["up arrow"] * 2 - held_keys["down arrow"] * 2
    if ursina.camera.zoom > -10: ursina.camera.zoom = -10
    if ursina.camera.zoom < -100: ursina.camera.zoom = -100
    player.move()
    player.check_collide(floor)

    # player.update()
    # print(player.position.x)
    ursina.camera.position = (player.position.x, player.position.y, ursina.camera.zoom)


app.run()
