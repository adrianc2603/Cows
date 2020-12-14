"""
#### GETTING PYTHON3 AND PYGAME ON LAPTOP
Download python3 (3.8)
python3 -m pip install -U pygame==2.0.0.dev6 --user

#### C0NVERTING PYTHON SCRIPT INTO EXEC FILE --- NOT WORKING ON MAC
install pyinstaller (pip3 install pyinstaller)
pyinstaller main.py --onefile --noconsole (in cows directory)
https://www.youtube.com/watch?v=lTxaran0Cig
"""
##=============================================================================
##                                1mm = 5px
##=============================================================================

import pygame
import player
import grass
import barrier_manager
import coin_manager
import enemy_manager
import screen_manager

# GLOBAL VARIABLES
LAST_LEVEL = 10 ##============================================================================================
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
screen_manager = screen_manager.ScreenManager()

# Set initial level
level = 1 ##============================================================================================
new_level = True

#=============================== MAIN GAMEPLAY ================================

running = True
while running:

    if new_level:
        barriers.clear()
        coins.clear()
        enemies.clear()

    # Set up level 1
    if level == 1 and new_level:
        player.level1()
        grass.level1()
        barriers = barrier_manager.level1()
        coins = coin_manager.level1()
        new_level = False
        
    # Set up level 2
    if level == 2 and new_level:
        player.level2()
        grass.level2()
        barriers = barrier_manager.level2()
        coins = coin_manager.level2()
        new_level = False

     # Set up level 3
    if level == 3 and new_level:
        screen_manager.blue_enemy_warning(screen)
        player.level3()
        grass.level3()
        barriers = barrier_manager.level3()
        coins = coin_manager.level3()
        enemies = enemy_manager.level3()
        new_level = False

    # Set up level 4
    if level == 4 and new_level:
        player.level4()
        grass.level4()
        barriers = barrier_manager.level4()
        coins = coin_manager.level4()
        enemies = enemy_manager.level4()
        new_level = False

    # Set up level 5
    if level == 5 and new_level:
        screen_manager.red_enemy_warning(screen)
        player.level5()
        grass.level5()
        barriers = barrier_manager.level5()
        coins = coin_manager.level5()
        enemies = enemy_manager.level5()
        new_level = False

    # Set up level 6
    if level == 6 and new_level:
        player.level6()
        grass.level6()
        barriers = barrier_manager.level6()
        coins = coin_manager.level6()
        enemies = enemy_manager.level6()
        new_level = False

    # Set up level 7
    if level == 7 and new_level:
        player.level7()
        grass.level7()
        barriers = barrier_manager.level7()
        coins = coin_manager.level7()
        enemies = enemy_manager.level7()
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