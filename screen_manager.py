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
    Display the start screen at the beginning of the game
    """
    def display_start_screen(self):
        while True:
            self.screen.fill(self.text_background)
            title = self.big_font.render("Welcome to Cows", True, self.text_colour, self.text_background)
            self.display_text(title, 350, 125)
            instructions = self.small_font.render("Make sure you've read the README.md file before you play the game", True, self.text_colour, self.text_background)
            self.display_text(instructions, 350, 225)
            start_play = self.small_font.render("Press ENTER/RETURN to begin the game", True, self.text_colour, self.text_background)
            self.display_text(start_play, 350, 325)
            pygame.display.update()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()    

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


    """
    Let the player enter their name to store their score in scores.txt file
    """
    def get_player_name(self):
        name = ""

        while True:

            self.screen.fill(self.text_background)
            please_display_name = self.big_font.render("Please enter your name:", True, self.text_colour, self.text_background)
            self.display_text(please_display_name, 360, 100)
            name_displayed = self.big_font.render(name, True, self.text_colour, self.text_background)
            self.display_text(name_displayed, 350, 250)
            pygame.display.update()

            """
            Please note this code was found on the following website and was not written by me:
            https://www.reddit.com/r/pygame/comments/205i05/get_user_input/
            """
            event = pygame.event.poll()
            keys = pygame.key.get_pressed()
            
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)  # Returns string id of pressed key.
                
                if len(key) == 1:  # This covers all letters and numbers not on numpad.
                    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                        name += key.upper()
                    else:
                        name += key
                elif key == "backspace":
                    name = name[:len(name) - 1]
                elif event.key == pygame.K_RETURN:  # Finished typing.
                    break
            """
            End of copied code
            """    
               
        return name    

    """
    Once the player finishes the game, display their results of the game
    """
    def display_results(self, name, time, wealth):
        while True:
            self.screen.fill(self.text_background)
            name_text = self.big_font.render("Name: " + name, True, self.text_colour, self.text_background)
            self.display_text(name_text, 340, 100)
            time_text = self.big_font.render("Time: " + str(time) + " seconds", True, self.text_colour, self.text_background)
            self.display_text(time_text, 340, 200)
            wealth_text = self.big_font.render("Wealth: $" + str(wealth), True, self.text_colour, self.text_background)
            self.display_text(wealth_text, 340, 300)
            score_location_text = self.small_font.render("You can find this information in the scores.txt file", True, self.text_colour, self.text_background)
            self.display_text(score_location_text, 340, 400)
            pygame.display.update()

            # Check if player has pressed exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
