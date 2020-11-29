import pygame

class Grass:

    """
    Constructor
    """
    def __init__(self):
        self.image = pygame.image.load("resources/grass.png")
        self.rectangle = self.image.get_rect()
        self.x = self.rectangle.left = 600
        self.y = self.rectangle.top = 410

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
        self.rectangle.bottom -= 20 # Approach grass from bottom

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
        self.rectangle.left = self.x # Can't approach from either side

    """
    Update the position of the grass's rectangle
    """
    def update_rectangle(self):
        self.rectangle.left = self.x + 20
        self.rectangle.top = self.y + 10

    """
    Return 1 if the player has reached the grass. Return 0 otherwise
    """
    def player_has_reached(self, player):
        if self.rectangle.colliderect(player.rectangle):
            return 1
        return 0