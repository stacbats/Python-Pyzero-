# pig shooting

import pgzrun

from random import randint
#       Variables
pig = Actor ("pig")
score = 0


# Main Program
def draw():
    screen.clear()
    pig.draw() 


def place_pig():
    pig.x= randint(10, 800)
    pig.y= randint(10,550)

def on_mouse_down(pos):
    if pig.collidepoint(pos):

        print("good shot!")
        place_pig()
        global score
        score = score + 1
        print(score)
    else:
        print(" you missed!")
        quit()



place_pig()


pgzrun.go()