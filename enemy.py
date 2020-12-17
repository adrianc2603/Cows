import pygame

class Enemy:

    """
    Constructor
    """
    def __init__(self, image, x, y, is_red = False):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.is_red = is_red
        self.rectangle = pygame.Rect(x + 7, y + 4, 40, 33) 
