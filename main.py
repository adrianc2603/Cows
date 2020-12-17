import pygame
import player
import grass
import barrier_manager
import coin_manager
import enemy_manager
import screen_manager
import level_manager

# GLOBAL VARIABLES
LAST_LEVEL = 10 
BACKGROUND = (124, 252 , 0)

# Initialise pygame and the screen
pygame.init()
screen = pygame.display.set_mode((700, 465))

# Initialise game caption and icon
pygame.display.set_caption("Cows")
icon = pygame.image.load("resources/icon.png")
pygame.display.set_icon(icon)

# Initialise player and grass objects
player = player.Player() 
grass = grass.Grass(player)

# Initialise barrier manager
barrier_manager = barrier_manager.BarrierManager(screen)
barriers = []

# Initialise coin manager
coin_manager = coin_manager.CoinManager(screen, player)
coins = []

# Initialise enemy manager
enemy_manager = enemy_manager.EnemyManager(screen, player)
enemies = []

# Initialise screen manager
screen_manager = screen_manager.ScreenManager(BACKGROUND, screen, player)

# Initialise level manager
level_manager = level_manager.LevelManager(player, grass, screen, screen_manager, barrier_manager, coin_manager, enemy_manager)

# Set initial level
level = 1 ##============================================================================================
new_level = True

#=============================== MAIN GAMEPLAY ================================

running = True
while running:

    if new_level:
        level_manager.setup_level(level)
        barriers = level_manager.get_level_barriers(level)
        coins = level_manager.get_level_coins(level)
        enemies = level_manager.get_level_enemies(level)
        new_level = False
        
    # Set screen colour as green
    screen.fill(BACKGROUND)

    # Display player wealth and current level 
    screen_manager.display_wealth_and_level(level)

    # Place player, grass, enemies, barriers and coins on screen
    screen.blit(player.image, (player.x, player.y))
    screen.blit(grass.image, (grass.x, grass.y))
    enemy_manager.draw(enemies)
    barrier_manager.draw(barriers)
    coin_manager.draw(coins)

    # Move player 
    player.move(barriers)

    # Update what is shown on the screen
    pygame.display.update()
  
    # Check if player reaches coin
    coin_manager.player_has_reached(coins)

    # Check if player reaches enemy
    enemy_manager.player_has_reached(enemies)

    # Display "Back to Level 1" message if player loses all their wealth
    if player.wealth < 0:
        screen_manager.display_back_to_level1()

    # Check if player reaches grass
    if grass.player_has_reached():
        level += 1
        new_level = True   

    # Check if player has exited game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if player has completed game
    if level > LAST_LEVEL:
        screen_manager.game_is_completed()
        running = False

    # Reset to level 1 if player wealth is below $0
    if player.wealth < 0:
        player.wealth = 0
        level = 1
        new_level = True