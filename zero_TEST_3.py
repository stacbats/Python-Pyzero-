#py game zero test

#from tkinter import X
import pgzrun       # import files to run the pyzero package
import random

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


    for index in range(0,len(squares)):
        squares[index].move()





def draw():                                             # create a function call draw
    
    # Clear screen
    screen.clear()
    for index in range(0,len(squares)):
        squares[index].render()


   


WIDTH = 500         # this is setting the window size
HEIGHT = 300

#(self,x,y,velX,velY,width,height, colour):
squares = []
for count in range(0,20):
    squares.append(Square(random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1),random.randint(1,5),
        random.randint(1,7),random.randint(5,50),random.randint(5,50),
        (random.randint(0,255),random.randint(0,255),random.randint(0,255))))


pgzrun.go()


