#py game zero test

import pgzrun       # import files to run the pyzero package


def update():
    pass


def draw():                                             # create a function call draw
    #draw a square
    rectangle = Rect((20,20),(15,15))                 ## first tuple is position of object, second is size
    screen.draw.filled_rect(rectangle, (255,0,0))

WIDTH = 500         # this is setting the window size
HEIGHT = 300

pgzrun.go()


