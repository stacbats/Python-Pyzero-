#py game zero test


import pgzrun       # import files to run the pyzero package


def update():
    global square_x, square_y, square_x_vel, square_y_vel
    square_x += square_x_vel 
 #   square_y +=1
    if square_x > WIDTH-square_width:
        square_x= WIDTH-square_width
        square_x_vel = -square_x_vel 
    elif square_x < 0:
        square_x=0
        square_x_vel= -square_x_vel

    square_y += square_y_vel
    if square_y > HEIGHT-square_width:
        square_y= HEIGHT-square_width
        square_y_vel = -square_y_vel 
    elif square_y < 0:
        square_y=0
        square_y_vel= -square_y_vel


    global REDsquare_x, REDsquare_y, REDsquare_x_vel, REDsquare_y_vel
    REDsquare_x += REDsquare_x_vel 
 #   square_y +=1
    if REDsquare_x > WIDTH-REDsquare_width:
        REDsquare_x= WIDTH-REDsquare_width
        REDsquare_x_vel = -REDsquare_x_vel 
    elif REDsquare_x < 0:
        REDsquare_x=0
        REDsquare_x_vel= -REDsquare_x_vel

    REDsquare_y += REDsquare_y_vel
    if REDsquare_y > HEIGHT-REDsquare_width:
        REDsquare_y= HEIGHT-REDsquare_width
        REDsquare_y_vel = -REDsquare_y_vel 
    elif REDsquare_y < 0:
        REDsquare_y=0
        REDsquare_y_vel= -REDsquare_y_vel


def draw():                                             # create a function call draw
    
    # Clear screen
    screen.clear()
    #draw a square
    rectangle = Rect((square_x,square_y),(square_width, square_height))                 ## first tuple is position of object, second is size
    screen.draw.filled_rect(rectangle, (50,0,120))
    BOX = Rect((REDsquare_x,REDsquare_y),(REDsquare_width, REDsquare_height))                 ## first tuple is position of object, second is size
    screen.draw.filled_rect(BOX, (255,0,0))

WIDTH = 500         # this is setting the window size
HEIGHT = 300

square_x = 0
square_x_vel = 3
square_y = 0
square_y_vel = 2
square_width = 15
square_height = 15

REDsquare_x = 0
REDsquare_x_vel = 6
REDsquare_y = 0
REDsquare_y_vel = 2
REDsquare_width = 10
REDsquare_height = 10

pgzrun.go()
