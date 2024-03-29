import pygame
import time

class Player:

    """
    Constructor
    """
    def __init__(self):
        self.image = pygame.image.load("resources/player.png")
        self.rectangle = self.image.get_rect()
        self.x = 10
        self.y = 8
        self.velocity = 2 
        self.wealth = 0

    """
    Level 1 Position
    """
    def level1(self):
        self.x = 10
        self.y = 8

    """
    Level 2 Position
    """
    def level2(self):
        self.x = 280
        self.y = 290

    """
    Level 3 Position
    """
    def level3(self):
        self.x = 10
        self.y = 323

    """
    Level 4 Position
    """
    def level4(self):
        self.x = 10
        self.y = 8

    """
    Level 5 Position
    """
    def level5(self):
        self.x = 10
        self.y = 201

    """
    Level 6 Position
    """
    def level6(self):
        self.x = 310
        self.y = 172

    """
    Level 7 Position
    """
    def level7(self):
        self.x = 108
        self.y = 258

    """
    Level 8 Position
    """
    def level8(self):
        self.x = 140
        self.y = 175

    """
    Level 9 Position
    """
    def level9(self):
        self.x = 310
        self.y = 218

    """
    Level 10 Position
    """
    def level10(self):
        self.x = 8
        self.y = 8

    """
    Move the player if there is no barrier in the way
    """
    def move(self, barriers):

        # Make sure player cannot move through a barrier
        no_left = no_right = no_up = no_down = False
        tolerance = self.velocity
        for b in barriers:
            if b.rectangle.colliderect(self.rectangle):
                if abs(b.rectangle.right - self.rectangle.left) <= tolerance:
                    no_left = True
                if abs(b.rectangle.left - self.rectangle.right) <= tolerance:
                    no_right = True
                if abs(b.rectangle.bottom - self.rectangle.top) <= tolerance:
                    no_up = True
                if abs(b.rectangle.top - self.rectangle.bottom) <= tolerance:
                    no_down = True

        # Move player the correct direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0 and not no_left:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.x < 640 and not no_right:
            self.x += self.velocity
        if keys[pygame.K_UP] and self.y > 0 and not no_up:
            self.y -= self.velocity
        if keys[pygame.K_DOWN] and self.y < 411 and not no_down:
            self.y += self.velocity  

        self.update_rectangle()

    """
    Update the position of the player's rectangle
    """
    def update_rectangle(self):
        self.rectangle.left = self.x
        self.rectangle.top = self.y

    """
    Add wealth to the player if they picked up a coin
    """
    def add_to_wealth(self, value):
        self.wealth += value

    """
    Remove wealth from the player if they collide with an enemy
    """
    def remove_wealth(self, enemy):
        
        # Blue enemy
        if (enemy.is_red == False):
            self.wealth -= 50 

        # Red enemy
        else:
            self.wealth = -1

           