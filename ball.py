import pygame
from random import randint

black = (0,0,0)

#class that represents a ball. derives from "Sprite" class in Python
class Ball(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):
        #Call the parent class (Sprite) constructor
        super().__init__()

        #Pass in the colour of the ball, its width and height
        #Set the background colour and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        #Draw the ball (rectangle)
        pygame.draw.rect(self.image, colour, [0,0, width, height])

        self.velocity = [randint(4,8), randint(-8,8)]

        #Fetch the rectangle object that has dimensions of image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)