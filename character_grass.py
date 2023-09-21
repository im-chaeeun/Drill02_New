from pico2d import *

open_canvas()

grass=load_image('grass.png')
cleae_canvas_now(400,30)
grass.draw_now(400, 90)
delay(1)

def run circle():
    print('CIRCLE')
    pass

def run_rectangle():
    print('RECTANGLE')
    pass

while True:
    run_circle()
    run_rectangle()

close_canvas()
