import pygame

class CoinManager:

    """
    Place all coins on the screen
    """
    def draw(screen, coins, player):

        gold = (212, 175, 55)
        silver = (192, 192, 192)
        bronze = (80, 50, 20)
        radius = 15

        for c in coins:

            # Gold coins
            if c[2] == 3: 
                pygame.draw.circle(screen, gold, [c[0], c[1]], radius)

            # Silver coins
            if c[2] == 2:
                pygame.draw.circle(screen, silver, [c[0], c[1]], radius)

            # Bronze coins
            if c[2] == 1:
                pygame.draw.circle(screen, bronze, [c[0], c[1]], radius)

    """
    Level 1 Coins
    """
    def level1():
        coins = []

        # Row 1
        coins.append([150, 35, 3])
        coins.append([350, 35, 2])
        coins.append([550, 35, 1])

        # Row 2
        coins.append([50, 115, 3])
        coins.append([250, 115, 2])
        coins.append([450, 115, 1])
        coins.append([650, 115, 3])

        # Row 3
        coins.append([150, 195, 3])
        coins.append([350, 195, 2])
        coins.append([550, 195, 1])

        # Row 4
        coins.append([50, 275, 3])
        coins.append([250, 275, 1])
        coins.append([450, 275, 2])
        coins.append([650, 275, 3])

        # Row 5
        coins.append([150, 355, 2])
        coins.append([350, 355, 3])
        coins.append([550, 355, 3])

        # Row 6
        coins.append([50, 435, 1])
        coins.append([250, 435, 2])
        coins.append([450, 435, 3])

        return coins

    """
    Level 2 Coins
    """
    def level2():
        coins = []

        # Row 1
        coins.append([55, 40, 1])
        coins.append([300, 40, 1])
        coins.append([550, 40, 2])

        # Row 2
        coins.append([200, 155, 3])
        coins.append([320, 155, 3])
        coins.append([465, 120, 2])
        coins.append([655, 175, 2])

        # Row 3
        coins.append([55, 240, 1])
        coins.append([165, 240, 1])
        coins.append([320, 240, 3])
        coins.append([560, 240, 3])

        # Row 4
        coins.append([160, 375, 2])
        coins.append([465, 325, 2])
        coins.append([560, 325, 3])

        # Row 5
        coins.append([260, 430, 1])
        coins.append([500, 420, 3])

        return coins

    """
    Level 3 Coins
    """
    def level3():
        coins = []

        # Row 1
        coins.append([45, 40, 3])
        coins.append([230, 40, 3])
        coins.append([380, 40, 2])
        coins.append([540, 40, 1])

        # Row 2
        coins.append([45, 120, 2])
        coins.append([360, 115, 3])
        coins.append([520, 115, 3])

        # Row 3
        coins.append([45, 200, 1])
        coins.append([140, 200, 2])
        coins.append([360, 195, 3])
        coins.append([520, 195, 3])

        # Row 4
        coins.append([440, 275, 1])
        coins.append([630, 260, 3])

        # Row 5
        coins.append([230, 345, 3])
        coins.append([440, 355, 2])
        coins.append([630, 355, 1])

        # Row 6
        coins.append([45, 425, 3])
        coins.append([210, 430, 2])
        coins.append([365, 430, 1])
        coins.append([535, 410, 1])

        return coins

    """
    Level 4 Coins
    """
    def level4():
        coins = []

        # Row 1
        coins.append([400, 35, 2])
        coins.append([550, 35, 2])

        # Row 2
        coins.append([50, 112, 3])
        coins.append([180, 112, 3])
        coins.append([330, 115, 3])
        coins.append([490, 130, 2])
        coins.append([630, 130, 1])

        # Row 3
        coins.append([42, 190, 3])
        coins.append([130, 190, 3])
        coins.append([645, 230, 1])

        # Row 4
        coins.append([42, 270, 3])
        coins.append([160, 268, 2])
        coins.append([310, 268, 1])
        coins.append([540, 300, 3])

        # Row 5
        coins.append([42, 350, 3])
        coins.append([160, 345, 2])
        coins.append([310, 345, 1])
        coins.append([540, 345, 3])
        coins.append([645, 330, 1])

        # Row 6
        coins.append([190, 425, 3])
        coins.append([340, 425, 3])
        coins.append([490, 425, 3])

        return coins

    """
    Level 5 Coins
    """
    def level5():
        coins = []

        # Row 1
        coins.append([50, 35, 3])
        coins.append([150, 35, 2])
        coins.append([250, 35, 1])
        coins.append([470, 35, 3])
        coins.append([570, 35, 3])
        coins.append([470, 80, 3])
        coins.append([570, 80, 3])

        # Row 2
        coins.append([100, 135, 2])
        coins.append([250, 135, 2])
        coins.append([460, 152, 1])
        coins.append([560, 152, 1])

        # Row 3
        coins.append([180, 230, 1])
        coins.append([345, 230, 1])

        # Row 4
        coins.append([75, 325, 1])
        coins.append([200, 300, 3])
        coins.append([200, 350, 3])
        coins.append([570, 300, 2])
        coins.append([570, 350, 2])
        coins.append([655, 300, 3])

        # Row 5
        coins.append([150, 422, 3])
        coins.append([250, 408, 3])
        coins.append([250, 444, 3])
        coins.append([560, 422, 1])
        coins.append([655, 380, 2])

        return coins

    """
    Level 6 Coins
    """
    def level6():
        coins = []

        # Row 1
        coins.append([45, 35, 1])
        coins.append([220, 35, 1])

        # Row 2
        coins.append([130, 120, 3])
        coins.append([325, 115, 3])
        coins.append([435, 115, 3])

        # Row 3
        coins.append([40, 280, 1])
        coins.append([130, 225, 2])
        coins.append([235, 200, 3])
        coins.append([655, 280, 1])

        # Row 4
        coins.append([40, 356, 2])
        coins.append([130, 356, 1])
        coins.append([255, 356, 2])
        coins.append([540, 356, 2])
        coins.append([655, 356, 2])

        # Row 5
        coins.append([40, 432, 3])
        coins.append([255, 432, 1])
        coins.append([385, 432, 2])
        coins.append([540, 432, 3])
        coins.append([655, 432, 3])

        return coins

    """
    Level 7 Coins
    """
    def level7():
        coins = []

        # Row 1
        coins.append([195, 35, 2])
        coins.append([333, 35, 3])
        coins.append([635, 35, 2])

        # Row 2
        coins.append([142, 110, 3])
        coins.append([410, 118, 3])
        coins.append([510, 118, 3])
        coins.append([640, 148, 1])

        # Row 3
        coins.append([380, 200, 2])
        coins.append([510, 200, 3])
       
        # Row 4
        coins.append([245, 280, 1])
        coins.append([445, 265, 1])
        coins.append([635, 260, 2])

        # Row 5
        coins.append([45, 352, 2])
        coins.append([445, 352, 3])

        # Row 6
        coins.append([245, 430, 1])
        coins.append([658, 430, 2])

        return coins

    """
    If a player has collected a coin, remove it from the screen and add 
    the coin's worth to the player's wealth
    """
    def player_has_reached(player, coins):
        radius = 15
        diameter = 30

        for c in coins:
            c_rect = pygame.Rect(c[0] - radius, c[1] - radius, diameter, diameter)
            if c_rect.colliderect(player.rectangle):
                player.add_to_wealth(c[2])
                coins.remove(c)