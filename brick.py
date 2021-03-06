import pygame
black = (0,0,0)

class Brick(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        self.rect = self.image.get_rect()