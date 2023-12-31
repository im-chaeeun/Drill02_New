import math
from pico2d import *

open_canvas(800, 600)
character=load_image('character.png')
grass=load_image('grass.png')

def render_frame(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.1)

def run_circle():
    print('CIRCLE')

    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 5):
        x=cx+r*math.cos(math.radians(deg))
        y=cy+r*math.sin(math.radians(deg))
        render_frame(x, y)
    pass

def run_rectangle():
    print('RECTANGLE')

    #bottom line
    for x in range(50, 750+1,5):
        render_frame(x, 90) # x, y 위치에 캐릭터를 그려줄 수 있는

    #right line
    for y in range(90, 550, 5):
        render_frame(750, y)
        
    #top line
    for x in range(750, 50-1, -5):
        render_frame(x, 550)

    #left line
    for y in range(550, 90, -5):
        render_frame(50, y)   

while True:
    run_circle()
    run_rectangle()
    break

close_canvas()
