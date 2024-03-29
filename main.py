import pygame
import player
import grass
import barrier_manager
import coin_manager
import enemy_manager
import screen_manager
import level_manager
import time

# GLOBAL VARIABLES
LAST_LEVEL = 10 
BACKGROUND = (255, 255 , 0)

# Initialise pygame and the screen
pygame.init()
screen = pygame.display.set_mode((700, 465))

# Initialise game caption and icon
pygame.display.set_caption("Cows")
icon = pygame.image.load("resources/player.png")
pygame.display.set_icon(icon)

# Initialise player and grass objects
player = player.Player() 
grass = grass.Grass(player)

# Initialise barrier manager and barriers list
barrier_manager = barrier_manager.BarrierManager(screen)
barriers = []

# Initialise coin manager and coins list
coin_manager = coin_manager.CoinManager(screen, player)
coins = []

# Initialise enemy manager and enemies list
enemy_manager = enemy_manager.EnemyManager(screen, player)
enemies = []

# Initialise screen manager
screen_manager = screen_manager.ScreenManager(BACKGROUND, screen, player)

# Initialise level manager
level_manager = level_manager.LevelManager(player, grass, screen, 
    screen_manager, barrier_manager, coin_manager, enemy_manager)

# Display the start screen
screen_manager.display_start_screen()

# Set initial level
level = 1
time_elapsed = 0
start_time = int(round(time.time()))
new_level = True

# #============================== MAIN GAMEPLAY ===============================

running = True
while running:

    # Player pauses game
    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        screen_manager.display_paused()

    # Setup the new level
    if new_level:
        level_manager.setup_level(level)
        barriers = level_manager.get_level_barriers(level)
        coins = level_manager.get_level_coins(level)
        enemies = level_manager.get_level_enemies(level)
        new_level = False
        
    # Set screen colour as yellow
    screen.fill(BACKGROUND)

    # Display player wealth, time elapsed and current level on the screen
    screen_manager.display_wealth_time_and_level(time_elapsed, level)

    # Place player, grass, enemies, barriers and coins on the screen
    screen.blit(player.image, (player.x, player.y))
    screen.blit(grass.image, (grass.x, grass.y))
    enemy_manager.draw(enemies)
    barrier_manager.draw(barriers)
    coin_manager.draw(coins)

    # Move the player 
    player.move(barriers)

    # Update what is shown on the screen
    pygame.display.update()
  
    # Check if the player reaches a coin
    coin_manager.player_has_reached(coins)

    # Check if the player reaches an enemy
    if enemy_manager.player_has_reached(enemies):
        time_elapsed += 5

    # Increment the time elapsed each second 
    if (start_time + 1) <= int(round(time.time())):
        time_elapsed += 1
        start_time = int(round(time.time()))

    # Check if the player reaches the grass
    if grass.player_has_reached():
        level += 1
        new_level = True   

    # Check if the player has exited the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # If player has completed the game, get their name and write their details 
    # to scores.txt, as well as displaying them on the screen
    if level > LAST_LEVEL:
        screen_manager.game_is_completed()
        name = screen_manager.get_player_name()

        # Write to the file
        f = open("scores.txt", "a")
        f.write("Name: " + name + " ----- Time: " + str(time_elapsed) + 
            " seconds ----- Wealth: $" + str(player.wealth) + "\n\n")
        f.close

        # Display results on screen until player presses exit
        screen_manager.display_results(name, time_elapsed, player.wealth)
        running = False

    # Reset to level 1 if the player's wealth is below $0
    if player.wealth < 0:
        screen_manager.display_back_to_level1()
        player.wealth = 0
        level = 1
        time_elapsed = 0
        start_time = int(round(time.time()))
        new_level = True        