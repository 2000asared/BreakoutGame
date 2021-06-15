#1 - Import Library
import pygame
from pygame.locals import *
from paddle import Paddle
from ball import Ball
from brick import Brick

#2 - Initialize the game
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout Game")

#3 - Initialise the colours
white = (255, 255, 255)
darkblue = (36, 90, 100)
lightblue = (0, 176, 240)
green = (8, 254, 0)
orange = (255, 182, 0)
yellow = (246, 254, 0)
red = (255, 0, 0)

score = 0
lives = 3

all_sprites_list = pygame.sprite.Group()

#Create the paddle
paddle = Paddle(lightblue, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

#Create the ball
ball = Ball(white, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(red, 80, 30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(yellow, 80, 30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(green, 80, 30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

all_sprites_list.add(paddle)
all_sprites_list.add(ball)

#used to continue loop until user leaves game.
carryOn = True

#the clock is used to control how fast screen updates
clock = pygame.time.Clock()

#-------------Main Program Loop--------------
while carryOn:
    #------Main event loop------------------
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: # if user clicked close
            carryOn = False #Flag that we are done so we exit this loop

    #----------Game Logic---------------
    #----sprite: a computer graphic which may be moved on-screen and otherwise manipulated
    #----as a single entity.

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    all_sprites_list.update()

    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, white)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            carryOn=False

    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    #Detect collisions between the ball and the paddle
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks)==0:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, white)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            carryOn=False


    #---------Drawing Code--------------
    screen.fill(darkblue)
    pygame.draw.line(screen, white, [0, 38], [800, 38], 2)

    #displays the score + number of lives at top of screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, white)
    screen.blit(text, (650, 10))

    all_sprites_list.draw(screen)
    #-----Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    #---- limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()







