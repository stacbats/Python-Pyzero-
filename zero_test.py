#py game zero test

#from tkinter import X
import pgzrun       # import files to run the pyzero package

class Square:

    #constructor
    def __init__(self,x,y,velX,velY,width,height, colour):
        self.x = x
        self.y = y
        self.x_vel = velX
        self.y_vel = velY
        self.width = width
        self.height = height
        self.colour = colour
    
    def move(self):
        self.x += self.x_vel
        if self.x > WIDTH - self.width:
            self.x= WIDTH-self.width
            self.x_vel =- self.x_vel 
        elif self.x < 0:
            self.x = 0
            self.x_vel= -self.x_vel

        self.y += self.y_vel
        if self.y > HEIGHT-self.width:
            self.y= HEIGHT-self.width
            self.y_vel = -self.y_vel 
        elif self.y < 0:
            self.y=0
            self.y_vel= -self.y_vel  

    def render(self):
        rectangle = Rect((self.x,self.y),(self.width, self.height))                 ## first tuple is position of object, second is size
        screen.draw.filled_rect(rectangle, (self.colour))                  

def update():
    global red_square, green_square,blue_square

    for index in range(0,len(squares)):
        squares[index].move()


# previously    red_square.move()



def draw():                                             # create a function call draw
    
    # Clear screen
    screen.clear()
    for index in range(0,len(squares)):
        squares[index].render()

# previously        green_square.render()
   


WIDTH = 500         # this is setting the window size
HEIGHT = 300
#  OBJECT DETAILS (x,y,velX,velY,width,height, colour)

red_square = Square(100,100,2,2,30,30,(255,0,0))
green_square = Square(5,5,1,18,10,14,(10,200,10))
blue_square = Square(20,5,9,1,20,15,(0,10,210))

squares = [red_square, green_square, blue_square]

pgzrun.go()


