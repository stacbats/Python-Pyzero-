# collecting Game

import pgzrun

from random import randint      # import Pythons random number function
#       Variables

WIDTH = 600
HEIGHT = 600
score = 0

game_over = False

fox = Actor ("fox")
fox.pos = 50, 100

carrot = Actor("carrot")
carrot.pos = 200, 200

# Main Program
def draw():
    screen.fill("green")
    fox.draw()
    carrot.draw() 
    screen.draw.text("SCORE: " + str(score), color="black", topleft=(400,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " +str(score), topleft = (150,300), fontsize = 60)

def place_carrot():
    carrot.x = randint(20, (WIDTH - 20))
    carrot.y = randint(20, (HEIGHT -20))
  

def time_up():
    global game_over
    game_over = True

def update():
    global score

    if keyboard.left:
        fox.x = fox.x -5
    elif keyboard.right:
        fox.x = fox.x +5
    elif keyboard.up:
        fox.y =fox.y -5
    elif keyboard.down:
        fox.y = fox.y +5

    carrot_collected = fox.colliderect(carrot)

    if carrot_collected:
        score = score + 10
        place_carrot()


    clock.schedule(time_up, 20.0)


pgzrun.go()

