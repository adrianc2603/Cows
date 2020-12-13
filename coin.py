import pygame

class Coin:

    """
    Constructor
    """
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.value = self.get_value()
        self.radius = 15
        self.diameter = 30
        self.rectangle = pygame.Rect(x - self.radius, y - self.radius, self.diameter, self.diameter)

    def get_value(self):
        if self.colour == (212, 175, 55): # Gold
            return 5
        if self.colour == (192, 192, 192): # Silver
            return 3
        if self.colour == (80, 50, 20): # Bronze
            return 1
            
