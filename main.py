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
grass = grass.Grass()

# Initialise barrier manager
barrier_manager = barrier_manager.BarrierManager()
barriers = []

# Initialise coin manager
coin_manager = coin_manager.CoinManager()
coins = []

# Initialise enemy manager
enemy_manager = enemy_manager.EnemyManager()
enemies = []

# Initialise screen manager
screen_manager = screen_manager.ScreenManager(BACKGROUND)

# Initialise level manager
level_manager = level_manager.LevelManager()

# Set initial level
level = 9 ##============================================================================================
new_level = True

#=============================== MAIN GAMEPLAY ================================

running = True
while running:

    if new_level:
        level_manager.setup_level(level, player, grass, screen_manager, screen)
        barriers = level_manager.get_level_barriers(level, barrier_manager)
        coins = level_manager.get_level_coins(level, coin_manager)
        enemies = level_manager.get_level_enemies(level, enemy_manager)
        new_level = False
        
    # Set screen colour as green
    screen.fill(BACKGROUND)

    # Display player wealth and current level 
    screen_manager.display_wealth_and_level(screen, level, player)

    # Place player, grass, enemies, barriers and coins on screen
    screen.blit(player.image, (player.x, player.y))
    screen.blit(grass.image, (grass.x, grass.y))
    enemy_manager.draw(screen, enemies)
    barrier_manager.draw(screen, barriers)
    coin_manager.draw(screen, coins)

    # Move player 
    player.move(barriers)

    # Update what is shown on the screen
    pygame.display.update()
  
    # Check if player reaches coin
    coin_manager.player_has_reached(player, coins)

    # Check if player reaches enemy
    enemy_manager.player_has_reached(player, enemies, screen, screen_manager)

    # Check if player reaches grass
    if grass.player_has_reached(player):
        level += 1
        new_level = True   

    # Check if player has exited game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if player has completed game
    if level > LAST_LEVEL:
        screen_manager.game_is_completed(screen)
        running = False

    # Reset to level 1 if player wealth is below $0
    if player.wealth < 0:
        player.wealth = 0
        level = 1
        new_level = True