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



def draw():                                             # create a function call draw
    
    # Clear screen
    screen.clear()
    #draw a square
    rectangle = Rect((square_x,square_y),(square_width, square_height))                 ## first tuple is position of object, second is size
    screen.draw.filled_rect(rectangle, (255,0,120))


WIDTH = 500         # this is setting the window size
HEIGHT = 300

square_x = 0
square_x_vel = 3
square_y = 0
square_y_vel = 2
square_width = 15
square_height = 15


pgzrun.go()


