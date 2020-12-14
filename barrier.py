import pygame

class Barrier:

    """
    Constructor
    """
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = (40, 26, 13) 
        self.rectangle = pygame.Rect(x, y, width, height)
