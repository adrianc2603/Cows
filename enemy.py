import pygame

class Enemy:

    """
    Constructor
    """
    def __init__(self, image, x, y):
        self.image_path = image
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect(x + 7, y + 4, 40, 33) 
