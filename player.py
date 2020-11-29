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
    Remove wealth from the player if they collide with a hole
    """
    def remove_wealth(self, num, screen, BLACK, BACKGROUND):
        
        # Black hole
        if (num == 1):
            self.wealth -= 50 

            # Display "There goes $50" message
            if (self.wealth >= 0):
                font = pygame.font.Font('freesansbold.ttf', 90)
                msg = font.render("There goes $50", True, BLACK, BACKGROUND)
                self.display_message_time_period(screen, msg, 350, 233, 3)

        # Red hole
        if (num == 2):
            self.wealth = -1

        # Display "Back to Level 1" message
        if self.wealth < 0:
            font = pygame.font.Font('freesansbold.ttf', 90)
            msg = font.render("Back to Level 1", True, BLACK, BACKGROUND)
            self.display_message_time_period(screen, msg, 350, 233, 3)

    """
    Display the player's wealth and current level at the top of the screen
    """
    def display_wealth_and_level(self, screen, level, BLACK, BACKGROUND):
        font = pygame.font.Font('freesansbold.ttf', 16)
        wealth = font.render("Wealth: $" + str(self.wealth), True, BLACK, BACKGROUND)
        self.display_text(screen, wealth, 175, 10)
        level = font.render("Level: " + str(level), True, BLACK, BACKGROUND)
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
    Warn the player that black holes steal $50
    """
    def black_hole_warning(self, screen, BLACK, BACKGROUND):
        font = pygame.font.Font('freesansbold.ttf', 32)
        msg = font.render("Black Holes Steal $50", True, BLACK, BACKGROUND)
        small_font = pygame.font.Font('freesansbold.ttf', 16)
        small_msg = small_font.render("If you go below $0, you go back to Level 1", True, BLACK, BACKGROUND)
        self.display_hole_waring(screen, msg, small_msg, BLACK, BACKGROUND)

    """ 
    Warn the player that red holes steal all your money and send you back to level 1
    """
    def red_hole_warning(self, screen, BLACK, RED, BACKGROUND):
        font = pygame.font.Font('freesansbold.ttf', 32)
        msg = font.render("Red Holes Steal All Your Money", True, BLACK, BACKGROUND)
        small_font = pygame.font.Font('freesansbold.ttf', 16)
        small_msg = small_font.render("You go back to Level 1", True, BLACK, BACKGROUND)
        self.display_hole_waring(screen, msg, small_msg, RED, BACKGROUND)

    """ 
    Given the messages to be displayed warning the player about the holes, 
    put these messages on the screen
    """
    def display_hole_waring(self, screen, msg, small_msg, COLOUR, BACKGROUND):
        start_time = int(round(time.time()))
        while ((start_time + 6) > int(round(time.time()))):
            screen.fill(BACKGROUND)
            pygame.draw.circle(screen, COLOUR, [350, 116], 30)
            self.display_text(screen, msg, 350, 233)
            self.display_text(screen, small_msg, 350, 280)
            pygame.display.update()

    """
    Display "You Win!" message on the screen and then exit the game
    """
    def game_is_completed(self, screen, BLACK, BACKGROUND):
        font = pygame.font.Font('freesansbold.ttf', 32)
        msg = font.render("You Win!", True, BLACK, BACKGROUND)
        screen.fill(BACKGROUND)
        self.display_message_time_period(screen, msg, 350, 233, 3)