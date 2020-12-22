import pygame

class Grass:

    """
    Constructor
    """
    def __init__(self, player):
        self.image = pygame.image.load("resources/grass.png")
        self.x = 600
        self.y = 410
        self.update_rectangle()
        self.player = player

    """
    Level 1 Position
    """
    def level1(self):
        self.x = 600
        self.y = 410
        self.update_rectangle()

    """
    Level 2 Position
    """
    def level2(self):
        self.x = 600
        self.y = 410
        self.update_rectangle()

    """
    Level 3 Position
    """
    def level3(self):
        self.x = 580 
        self.y = 90 
        self.update_rectangle()

    """
    Level 4 Position
    """
    def level4(self):
        self.x = 600
        self.y = 410
        self.update_rectangle()

    """
    Level 5 Position
    """
    def level5(self):
        self.x = 600
        self.y = 207
        self.update_rectangle()

    """
    Level 6 Position
    """
    def level6(self):
        self.x = 600
        self.y = 15
        self.update_rectangle()

    """
    Level 7 Position
    """
    def level7(self):
        self.x = 87
        self.y = 195
        self.update_rectangle()

    """
    Level 8 Position
    """
    def level8(self):
        self.x = 252
        self.y = 115
        self.update_rectangle()

    """
    Level 9 Position
    """
    def level9(self):
        self.x = -5
        self.y = 20
        self.update_rectangle()    

    """
    Level 10 Position
    """
    def level10(self):
        self.x = 515
        self.y = 410
        self.update_rectangle()        

    """
    Update the position of the grass's rectangle
    """
    def update_rectangle(self):
        self.rectangle = pygame.Rect(self.x + 20, self.y + 10, 54, 20)

    """
    Return True if the player has reached the grass. Return False otherwise
    """
    def player_has_reached(self):
        if self.rectangle.colliderect(self.player.rectangle):
            return True
        return False