import pygame

class Grass:

    """
    Constructor
    """
    def __init__(self):
        self.image = pygame.image.load("resources/grass.png")
        self.x = 600
        self.y = 410
        self.update_rectangle()

    """
    Level 1 Postion
    """
    def level1(self):
        self.x = 600
        self.y = 410
        self.update_rectangle()

    """
    Level 2 Postion
    """
    def level2(self):
        self.x = 600
        self.y = 410
        self.update_rectangle()

    """
    Level 3 Postion
    """
    def level3(self):
        self.x = 580 
        self.y = 90 
        self.update_rectangle()

    """
    Level 4 Postion
    """
    def level4(self):
        self.x = 600
        self.y = 410
        self.update_rectangle()

    """
    Level 5 Postion
    """
    def level5(self):
        self.x = 600
        self.y = 207
        self.update_rectangle()

    """
    Level 6 Postion
    """
    def level6(self):
        self.x = 600
        self.y = 15
        self.update_rectangle()

    """
    Level 7 Postion
    """
    def level7(self):
        self.x = 87
        self.y = 195
        self.update_rectangle()

    """
    Level 8 Postion
    """
    def level8(self):
        self.x = 252
        self.y = 115
        self.update_rectangle()

    """
    Update the position of the grass's rectangle
    """
    def update_rectangle(self):
        self.rectangle = pygame.Rect(self.x + 20, self.y + 10, 54, 20)

    """
    Return 1 if the player has reached the grass. Return 0 otherwise
    """
    def player_has_reached(self, player):
        if self.rectangle.colliderect(player.rectangle):
            return 1
        return 0