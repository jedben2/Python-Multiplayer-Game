import dataclasses
import socket
from ursina import *
from client_mods.player import *
from client_mods.arrow import *
import sys

ID = '1'
HOST = '127.0.0.1'
PORT = 2000

def update():
    print("hello?")
    go = s.recv(1024)
    print("recieved, send: " + f"{players[0].intersects(floor).hit}/{held_keys}")
    s.send(f"{players[0].intersects(floor).hit}/{held_keys}".encode())
    print("sent")
    # for player in players:
    #     thing = s.recv(1024).decode().split('/')
    #     print(f"thing {thing}")
    #     player.position = (float(thing[0]), float(thing[1]))
    #     player.frame = thing[2]
    #     player.direction = thing[3]
    #     player.frame = int(player.frame)
    #     player.flip()
    #     print("done " + player.__repr__())
    thing = s.recv(1024).decode().split('/')
    print(f"thing {thing}")
    players[0].position = (float(thing[0]), float(thing[1]))
    players[0].frame = thing[2]
    players[0].direction = thing[3]
    players[0].frame = int(players[0].frame)
    players[0].flip()
    print("done " + players[0].__repr__())

    # if held_keys['w']:
    #     s.send("exit".encode())
    #     s.close()
    #     sys.exit()


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

    players = [Player(position=(-5, 0), model="quad", texture="textures//char1_right.png", collider='box', scale_x=1,
                      scale_y=1, char_num="1"),
               Player(position=(5, 0), model="quad", texture="textures//char2_left.png", collider='box', scale_x=1,
                      scale_y=1, char_num="2")]
    players[1].disable()
    floor = Entity(position=(0, -1), model="quad", scale_x=30, collider='box')
    arrow = [Arrow_Body(players[0]), Arrow_Head(players[0])]
    ursina.camera.position = (players[0].position.x, players[0].position.y, -30)
    camera.add_script(SmoothFollow(target=players[0], offset=[0, 0, -30], speed=10))

    app.run()
    print("closed")
