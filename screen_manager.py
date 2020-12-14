import pygame
import time

class ScreenManager:

    """
    Constructor
    """
    def __init__(self):
        self.text_colour = (0, 0, 0) # Black
        self.text_background = (124, 252 , 0) # Screen background
        self.big_font = pygame.font.Font('freesansbold.ttf', 32)
        self.small_font = pygame.font.Font('freesansbold.ttf', 16)

    """
    Display the player's wealth and current level at the top of the screen
    """
    def display_wealth_and_level(self, screen, level, player):
        wealth = self.small_font.render("Wealth: $" + str(player.wealth), True, self.text_colour, self.text_background)
        self.display_text(screen, wealth, 175, 10)
        level = self.small_font.render("Level: " + str(level), True, self.text_colour, self.text_background)
        self.display_text(screen, level, 525, 10)

    """
    Display the given message on the screen
    """
    def display_text(self, screen, msg, x, y):
        rect = msg.get_rect()
        rect.center = (x, y)
        screen.blit(msg, rect)

    """
    Display the given message on the screen for a specified time period
    """
    def display_message_time_period(self, screen, msg, x, y, duration):
        start_time = int(round(time.time()))
        while ((start_time + duration) > int(round(time.time()))):
                self.display_text(screen, msg, x, y)
                pygame.display.update()
        
    """ 
    Warn the player that blue enemies steal $50
    """
    def blue_enemy_warning(self, screen):
        msg = self.big_font.render("Blue Enemies Steal $50", True, self.text_colour, self.text_background)
        small_msg = self.small_font.render("If you go below $0, you go back to Level 1", True, self.text_colour, self.text_background)
        self.display_enemy_warning(screen, msg, small_msg, pygame.image.load("resources/blue_enemy.png"))

    """ 
    Warn the player that red enemies steal all your money and send you back to level 1
    """
    def red_enemy_warning(self, screen):
        msg = self.big_font.render("Red Enemies Steal All Your Money", True, self.text_colour, self.text_background)
        small_msg = self.small_font.render("You go back to Level 1", True, self.text_colour, self.text_background)
        self.display_enemy_warning(screen, msg, small_msg, pygame.image.load("resources/red_enemy.png"))

    """ 
    Given the messages to be displayed warning the player about the enemies, 
    put these messages on the screen
    """
    def display_enemy_warning(self, screen, msg, small_msg, image):
        start_time = int(round(time.time()))
        while ((start_time + 6) > int(round(time.time()))):
            screen.fill(self.text_background)
            screen.blit(image, (320, 86))
            self.display_text(screen, msg, 350, 233)
            self.display_text(screen, small_msg, 350, 280)
            pygame.display.update()

    """
    Display this message when a player loses $50 by colliding with a blue enemy
    """
    def display_message_lost_wealth(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 90)
        msg = font.render("There goes $50", True, self.text_colour, self.text_background)
        self.display_message_time_period(screen, msg, 350, 233, 3)

    """
    Display this message when a player goes back to level 1 by colliding with a red enemy
    """
    def display_back_to_level1(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 90)
        msg = font.render("Back to Level 1", True, self.text_colour, self.text_background)
        self.display_message_time_period(screen, msg, 350, 233, 3)

    """
    Display "You Win!" message on the screen and then exit the game
    """
    def game_is_completed(self, screen):
        msg = self.big_font.render("You Win!", True, self.text_colour, self.text_background)
        screen.fill(self.text_background)
        self.display_message_time_period(screen, msg, 350, 233, 3)
