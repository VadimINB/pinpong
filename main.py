from pygame import *

SCREENSIZE = (700, 700)
BGCOLOR = (255,255,255)

window = display.set_mode(SCREENSIZE)
display.set_caption('pin-pong')
timer = time.Clock()

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


    
    window.fill(BGCOLOR)
    display.update()
    timer.tick(60)