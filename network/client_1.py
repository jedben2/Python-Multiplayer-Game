import socket
from ursina import *
from game_mods.player import *
from game_mods.arrow import *

ID = '1'
HOST = '127.0.0.1'
PORT = 2000

def update():
    s.send(f"{ID}/{players[0].position}/{players[0].frame}/{players[0].hp}/{players[0].dx}/{players[0].dy}/{players[0].intersects(floor).hit}".encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    app = Ursina()
    window.vsync = 60
    window.title = 'Multiplayer Game Client 1'
    window.borderless = False
    window.fullscreen_size = (1920, 1080)
    window.fullscreen = True
    window.exit_button.visible = True
    window.fps_counter.enabled = True

    players = [Player(position=(-5, 0), model="quad", texture="textures/char1_right.png", collider='box', scale_x=1,
                      scale_y=1, char_num="1"),
               Player(position=(5, 0), model="quad", texture="textures/char2_left.png", collider='box', scale_x=1,
                      scale_y=1, char_num="2")]
    floor = Entity(position=(0, -1), model="quad", scale_x=30, collider='box')
    arrow = [Arrow_Body(players[0]), Arrow_Head(players[0])]
    ursina.camera.position = (players[0].position.x, players[0].position.y, -30)
    camera.add_script(SmoothFollow(target=players[0], offset=[0, 0, -30], speed=10))

    app.run()
    print("closed")
