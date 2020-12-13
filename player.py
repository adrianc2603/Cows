import pygame
import time

class Player:

    """
    Constructor
    """
    def __init__(self):
        self.image = pygame.image.load("resources/player.png")
        self.rectangle = self.image.get_rect()
        self.x = self.rectangle.left = 10
        self.y = self.rectangle.top = 10
        self.velocity = 2 
        self.wealth = 0

    """
    Level 1 Postion
    """
    def level1(self):
        self.x = 10
        self.y = 5

    """
    Level 2 Postion
    """
    def level2(self):
        self.x = 280
        self.y = 290

    """
    Level 3 Postion
    """
    def level3(self):
        self.x = 10
        self.y = 320

    """
    Level 4 Postion
    """
    def level4(self):
        self.x = 10
        self.y = 5

    """
    Level 5 Postion
    """
    def level5(self):
        self.x = 10
        self.y = 198

    """
    Level 6 Postion
    """
    def level6(self):
        self.x = 310
        self.y = 169

    """
    Level 7 Postion
    """
    def level7(self):
        self.x = 110
        self.y = 255

    """
    Move the player if there is no barrier in the way
    """
    def move(self, barriers):

        # Make sure player cannot move through barrier
        no_left = no_right = no_up = no_down = False
        tolerance = 2
        for b in barriers:
            b_rect = pygame.Rect(b[0], b[1], b[2], b[3])
            if b_rect.colliderect(self.rectangle):
                if abs(b_rect.right - self.rectangle.left) <= tolerance:
                    no_left = True
                if abs(b_rect.left - self.rectangle.right) <= tolerance:
                    no_right = True
                if abs(b_rect.bottom - self.rectangle.top) <= tolerance:
                    no_up = True
                if abs(b_rect.top - self.rectangle.bottom) <= tolerance:
                    no_down = True

        # Move player the correct direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0 and not no_left:
            self.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.x < 640 and not no_right:
            self.x += self.velocity
        if keys[pygame.K_UP] and self.y > 0 and not no_up:
            self.y -= self.velocity
        if keys[pygame.K_DOWN] and self.y < 402 and not no_down:
            self.y += self.velocity  

        self.update_rectangle()

    """
    Update the position of the player's rectangle
    """
    def update_rectangle(self):
        self.rectangle.left = self.x
        self.rectangle.top = self.y

    """
    Add wealth to the player if they pick up coins
    """
    def add_to_wealth(self, num):

        # Gold coin
        if num == 3:
            self.wealth += 5

        # Silver coin
        if num == 2:
            self.wealth += 3

        # Bronze coin
        if num == 1:
            self.wealth += 1

    """
    Remove wealth from the player if they collide with an enemy
    """
    def remove_wealth(self, enemy_image_path, screen, screen_manager):
        
        # Blue enemy
        if (enemy_image_path == "resources/blue_enemy.png"):
            self.wealth -= 50 

            # Display "There goes $50" message
            if (self.wealth >= 0):
                screen_manager.display_message_lost_wealth(screen)

        # Red enemy
        if (enemy_image_path == "resources/red_enemy.png"):
            self.wealth = -1

        # Display "Back to Level 1" message
        if self.wealth < 0:
            screen_manager.display_back_to_level1(screen)
           