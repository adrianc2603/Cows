import pygame

class Grass:

    """
    Constructor
    """
    def __init__(self, player):
        self.image = pygame.image.load("resources/grass.png")
        self.x = 600
        self.y = 400
        self.update_rectangle()
        self.player = player

    """
    Level 1 Position
    """
    def level1(self):
        self.x = 600
        self.y = 400
        self.update_rectangle()

    """
    Level 2 Position
    """
    def level2(self):
        self.x = 615
        self.y = 390
        self.update_rectangle()

    """
    Level 3 Position
    """
    def level3(self):
        self.x = 600 
        self.y = 90 
        self.update_rectangle()

    """
    Level 4 Position
    """
    def level4(self):
        self.x = 610
        self.y = 395
        self.update_rectangle()

    """
    Level 5 Position
    """
    def level5(self):
        self.x = 618
        self.y = 197
        self.update_rectangle()

    """
    Level 6 Position
    """
    def level6(self):
        self.x = 616
        self.y = 5
        self.update_rectangle()

    """
    Level 7 Position
    """
    def level7(self):
        self.x = 103
        self.y = 175
        self.update_rectangle()

    """
    Level 8 Position
    """
    def level8(self):
        self.x = 267
        self.y = 95
        self.update_rectangle()

    """
    Level 9 Position
    """
    def level9(self):
        self.x = 10
        self.y = 5
        self.update_rectangle()    

    """
    Level 10 Position
    """
    def level10(self):
        self.x = 534
        self.y = 397
        self.update_rectangle()        

    """
    Update the position of the grass's rectangle
    """
    def update_rectangle(self):
        self.rectangle = pygame.Rect(self.x + 10, self.y + 10, 40, 45)

    """
    Return True if the player has reached the grass. Return False otherwise
    """
    def player_has_reached(self):
        if self.rectangle.colliderect(self.player.rectangle):
            return True
        return False