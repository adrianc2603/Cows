import pygame
import time

class ScreenManager:

    """
    Constructor
    """
    def __init__(self, BACKGROUND, screen, player):
        self.text_colour = (0, 0, 0) # Black
        self.text_background = BACKGROUND 
        self.big_font = pygame.font.Font('freesansbold.ttf', 32)
        self.small_font = pygame.font.Font('freesansbold.ttf', 16)
        self.screen = screen
        self.player = player

    """
    Display the player's wealth, time elapsed and current level at the top of the screen
    """
    def display_wealth_time_and_level(self, time_elapsed, level):
        wealth = self.small_font.render("Wealth: $" + str(self.player.wealth), True, self.text_colour, self.text_background)
        self.display_text(wealth, 175, 10)
        time = self.small_font.render("Time: " + str(time_elapsed), True, self.text_colour, self.text_background)
        self.display_text(time, 350, 10)
        level = self.small_font.render("Level: " + str(level), True, self.text_colour, self.text_background)
        self.display_text(level, 525, 10)
       
    """
    Display the given message on the screen
    """
    def display_text(self, msg, x, y):
        rect = msg.get_rect()
        rect.center = (x, y)
        self.screen.blit(msg, rect)

    """
    Display the given message on the screen for a specified time period
    """
    def display_message_time_period(self, msg, x, y, duration):
        start_time = int(round(time.time()))
        while ((start_time + duration) > int(round(time.time()))):
                self.display_text(msg, x, y)
                pygame.display.update()
        
    """ 
    Warn the player that blue enemies steal $50
    """
    def blue_enemy_warning(self):
        msg = self.big_font.render("Blue Enemies Steal $50", True, self.text_colour, self.text_background)
        small_msg = self.small_font.render("If you go below $0, you go back to Level 1", True, self.text_colour, self.text_background)
        self.display_enemy_warning(msg, small_msg, pygame.image.load("resources/blue_enemy.png"))

    """ 
    Warn the player that red enemies steal all your money and send you back to level 1
    """
    def red_enemy_warning(self):
        msg = self.big_font.render("Red Enemies Steal All Your Money", True, self.text_colour, self.text_background)
        small_msg = self.small_font.render("You go back to Level 1", True, self.text_colour, self.text_background)
        self.display_enemy_warning(msg, small_msg, pygame.image.load("resources/red_enemy.png"))

    """ 
    Given the messages to be displayed warning the player about the enemies, 
    put these messages on the screen
    """
    def display_enemy_warning(self, msg, small_msg, image):
        start_time = int(round(time.time()))
        while ((start_time + 6) > int(round(time.time()))):
            self.screen.fill(self.text_background)
            self.screen.blit(image, (320, 86))
            self.display_text(msg, 350, 233)
            self.display_text(small_msg, 350, 280)
            pygame.display.update()

    """
    Display this message when a player goes back to level 1 by colliding with a red enemy
    """
    def display_back_to_level1(self):
        msg = self.big_font.render("Back to Level 1", True, self.text_colour, self.text_background)
        self.screen.fill(self.text_background)
        self.display_message_time_period(msg, 350, 233, 3)


    """
    Display "You Win!" message on the screen and then exit the game
    """
    def game_is_completed(self):
        msg = self.big_font.render("You Win!", True, self.text_colour, self.text_background)
        self.screen.fill(self.text_background)
        self.display_message_time_period(msg, 350, 233, 3)
