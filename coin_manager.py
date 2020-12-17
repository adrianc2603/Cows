import pygame
import coin

class CoinManager:

    """
    Constructor
    """
    def __init__(self):
        self.gold = (212, 175, 55)
        self.silver = (192, 192, 192)
        self.bronze = (80, 50, 20)

    """
    Place all coins on the screen
    """
    def draw(self, screen, coins):
        for c in coins:
            pygame.draw.circle(screen, c.colour, [c.x, c.y], c.radius)

    """
    Level 1 Coins
    """
    def level1(self):
        coins = []

        # Row 1
        coins.append(coin.Coin(150, 35, self.gold))
        coins.append(coin.Coin(350, 35, self.silver))
        coins.append(coin.Coin(550, 35, self.bronze))

        # Row 2
        coins.append(coin.Coin(50, 115, self.gold))
        coins.append(coin.Coin(250, 115, self.silver))
        coins.append(coin.Coin(450, 115, self.bronze))
        coins.append(coin.Coin(650, 115, self.gold))

        # Row 3
        coins.append(coin.Coin(150, 195, self.gold))
        coins.append(coin.Coin(350, 195, self.silver))
        coins.append(coin.Coin(550, 195, self.bronze))

        # Row 4
        coins.append(coin.Coin(50, 275, self.gold))
        coins.append(coin.Coin(250, 275, self.bronze))
        coins.append(coin.Coin(450, 275, self.silver))
        coins.append(coin.Coin(650, 275, self.gold))

        # Row 5
        coins.append(coin.Coin(150, 355, self.silver))
        coins.append(coin.Coin(350, 355, self.gold))
        coins.append(coin.Coin(550, 355, self.gold))

        # Row 6
        coins.append(coin.Coin(50, 435, self.bronze))
        coins.append(coin.Coin(250, 435, self.silver))
        coins.append(coin.Coin(450, 435, self.gold))

        return coins

    """
    Level 2 Coins
    """
    def level2(self):
        coins = []

        # Row 1
        coins.append(coin.Coin(55, 40, self.bronze))
        coins.append(coin.Coin(300, 40, self.bronze))
        coins.append(coin.Coin(550, 40, self.silver))

        # Row 2
        coins.append(coin.Coin(200, 155, self.gold))
        coins.append(coin.Coin(320, 155, self.gold))
        coins.append(coin.Coin(465, 120, self.silver))
        coins.append(coin.Coin(655, 175, self.silver))

        # Row 3
        coins.append(coin.Coin(55, 240, self.bronze))
        coins.append(coin.Coin(165, 240, self.bronze))
        coins.append(coin.Coin(320, 240, self.gold))
        coins.append(coin.Coin(560, 240, self.gold))

        # Row 4
        coins.append(coin.Coin(160, 375, self.silver))
        coins.append(coin.Coin(465, 325, self.silver))
        coins.append(coin.Coin(560, 325, self.gold))

        # Row 5
        coins.append(coin.Coin(260, 430, self.bronze))
        coins.append(coin.Coin(500, 420, self.gold))

        return coins

    """
    Level 3 Coins
    """
    def level3(self):
        coins = []

        # Row 1
        coins.append(coin.Coin(45, 40, self.gold))
        coins.append(coin.Coin(230, 40, self.gold))
        coins.append(coin.Coin(380, 40, self.silver))
        coins.append(coin.Coin(540, 40, self.bronze))

        # Row 2
        coins.append(coin.Coin(45, 120, self.silver))
        coins.append(coin.Coin(360, 115, self.gold))
        coins.append(coin.Coin(520, 115, self.gold))

        # Row 3
        coins.append(coin.Coin(45, 200, self.bronze))
        coins.append(coin.Coin(140, 200, self.silver))
        coins.append(coin.Coin(360, 195, self.gold))
        coins.append(coin.Coin(520, 195, self.gold))

        # Row 4
        coins.append(coin.Coin(440, 275, self.bronze))
        coins.append(coin.Coin(630, 260, self.gold))

        # Row 5
        coins.append(coin.Coin(230, 345, self.gold))
        coins.append(coin.Coin(440, 355, self.silver))
        coins.append(coin.Coin(630, 355, self.bronze))

        # Row 6
        coins.append(coin.Coin(45, 425, self.gold))
        coins.append(coin.Coin(210, 430, self.silver))
        coins.append(coin.Coin(365, 430, self.bronze))
        coins.append(coin.Coin(535, 410, self.bronze))

        return coins

    """
    Level 4 Coins
    """
    def level4(self):
        coins = []

        # Row 1
        coins.append(coin.Coin(400, 35, self.silver))
        coins.append(coin.Coin(550, 35, self.silver))

        # Row 2
        coins.append(coin.Coin(50, 112, self.gold))
        coins.append(coin.Coin(180, 112, self.gold))
        coins.append(coin.Coin(330, 115, self.gold))
        coins.append(coin.Coin(490, 130, self.silver))
        coins.append(coin.Coin(630, 130, self.bronze))

        # Row 3
        coins.append(coin.Coin(42, 190, self.gold))
        coins.append(coin.Coin(130, 190, self.gold))
        coins.append(coin.Coin(645, 230, self.bronze))

        # Row 4
        coins.append(coin.Coin(42, 270, self.gold))
        coins.append(coin.Coin(160, 268, self.silver))
        coins.append(coin.Coin(310, 268, self.bronze))
        coins.append(coin.Coin(540, 300, self.gold))

        # Row 5
        coins.append(coin.Coin(42, 350, self.gold))
        coins.append(coin.Coin(160, 345, self.silver))
        coins.append(coin.Coin(310, 345, self.bronze))
        coins.append(coin.Coin(540, 345, self.gold))
        coins.append(coin.Coin(645, 330, self.bronze))

        # Row 6
        coins.append(coin.Coin(190, 425, self.gold))
        coins.append(coin.Coin(340, 425, self.gold))
        coins.append(coin.Coin(490, 425, self.gold))

        return coins

    """
    Level 5 Coins
    """
    def level5(self):
        coins = []

        # Row 1
        coins.append(coin.Coin(50, 35, self.gold))
        coins.append(coin.Coin(150, 35, self.silver))
        coins.append(coin.Coin(250, 35, self.bronze))
        coins.append(coin.Coin(470, 35, self.gold))
        coins.append(coin.Coin(570, 35, self.gold))
        coins.append(coin.Coin(470, 80, self.gold))
        coins.append(coin.Coin(570, 80, self.gold))

        # Row 2
        coins.append(coin.Coin(100, 135, self.silver))
        coins.append(coin.Coin(250, 135, self.silver))
        coins.append(coin.Coin(460, 152, self.bronze))
        coins.append(coin.Coin(560, 152, self.bronze))

        # Row 3
        coins.append(coin.Coin(180, 230, self.bronze))
        coins.append(coin.Coin(345, 230, self.bronze))

        # Row 4
        coins.append(coin.Coin(75, 325, self.bronze))
        coins.append(coin.Coin(200, 300, self.gold))
        coins.append(coin.Coin(200, 350, self.gold))
        coins.append(coin.Coin(570, 300, self.silver))
        coins.append(coin.Coin(570, 350, self.silver))
        coins.append(coin.Coin(655, 300, self.gold))

        # Row 5
        coins.append(coin.Coin(150, 422, self.gold))
        coins.append(coin.Coin(250, 408, self.gold))
        coins.append(coin.Coin(250, 444, self.gold))
        coins.append(coin.Coin(560, 422, self.bronze))
        coins.append(coin.Coin(655, 380, self.silver))

        return coins

    """
    Level 6 Coins
    """
    def level6(self):
        coins = []

        # Row 1
        coins.append(coin.Coin(45, 35, self.bronze))
        coins.append(coin.Coin(220, 35, self.bronze))

        # Row 2
        coins.append(coin.Coin(130, 120, self.gold))
        coins.append(coin.Coin(325, 115, self.gold))
        coins.append(coin.Coin(435, 115, self.gold))

        # Row 3
        coins.append(coin.Coin(40, 280, self.bronze))
        coins.append(coin.Coin(130, 225, self.silver))
        coins.append(coin.Coin(235, 200, self.gold))
        coins.append(coin.Coin(655, 280, self.bronze))

        # Row 4
        coins.append(coin.Coin(40, 356, self.silver))
        coins.append(coin.Coin(130, 356, self.bronze))
        coins.append(coin.Coin(255, 356, self.silver))
        coins.append(coin.Coin(540, 356, self.silver))
        coins.append(coin.Coin(655, 356, self.silver))

        # Row 5
        coins.append(coin.Coin(40, 432, self.gold))
        coins.append(coin.Coin(255, 432, self.bronze))
        coins.append(coin.Coin(385, 432, self.silver))
        coins.append(coin.Coin(540, 432, self.gold))
        coins.append(coin.Coin(655, 432, self.gold))

        return coins

    """
    Level 7 Coins
    """
    def level7(self):
        coins = []

        # Row 1
        coins.append(coin.Coin(195, 35, self.silver))
        coins.append(coin.Coin(333, 35, self.gold))
        coins.append(coin.Coin(635, 35, self.silver))

        # Row 2
        coins.append(coin.Coin(142, 110, self.gold))
        coins.append(coin.Coin(410, 118, self.gold))
        coins.append(coin.Coin(510, 118, self.gold))
        coins.append(coin.Coin(640, 148, self.bronze))

        # Row 3
        coins.append(coin.Coin(380, 200, self.silver))
        coins.append(coin.Coin(510, 200, self.gold))
       
        # Row 4
        coins.append(coin.Coin(245, 280, self.bronze))
        coins.append(coin.Coin(445, 265, self.bronze))
        coins.append(coin.Coin(635, 260, self.silver))

        # Row 5
        coins.append(coin.Coin(45, 352, self.silver))
        coins.append(coin.Coin(445, 352, self.gold))

        # Row 6
        coins.append(coin.Coin(245, 430, self.bronze))
        coins.append(coin.Coin(658, 430, self.silver))

        return coins

    """
    Level 8 Coins
    """
    def level8(self):
        coins = []

        # Row 1
        coins.append(coin.Coin(130, 35, self.silver))
        coins.append(coin.Coin(425, 40, self.silver))
        coins.append(coin.Coin(645, 40, self.bronze))

        # Row 2
        coins.append(coin.Coin(395, 130, self.bronze))
        coins.append(coin.Coin(460, 130, self.bronze))
        coins.append(coin.Coin(645, 130, self.silver))

        # Row 3
        coins.append(coin.Coin(48, 210, self.gold))
        coins.append(coin.Coin(645, 250, self.bronze))
       
        # Row 4
        coins.append(coin.Coin(48, 280, self.gold))
        coins.append(coin.Coin(178, 280, self.gold))
        coins.append(coin.Coin(300, 280, self.gold))

        # Row 5
        coins.append(coin.Coin(48, 350, self.gold))
        coins.append(coin.Coin(178, 350, self.gold))
        coins.append(coin.Coin(300, 350, self.gold))

        # Row 6
        coins.append(coin.Coin(48, 420, self.gold))
        coins.append(coin.Coin(178, 420, self.gold))
        coins.append(coin.Coin(300, 420, self.gold))

        return coins    

    """
    Level 9 Coins
    """
    def level9(self):
        coins = []

        # Row 1
        coins.append(coin.Coin(150, 50, self.bronze))
        coins.append(coin.Coin(280, 50, self.gold))
        coins.append(coin.Coin(410, 50, self.silver))
        coins.append(coin.Coin(540, 50, self.gold))

        # Row 2
        coins.append(coin.Coin(390, 160, self.gold))
        coins.append(coin.Coin(648, 160, self.silver))
        
        # Row 3
        coins.append(coin.Coin(50, 250, self.gold))
        coins.append(coin.Coin(145, 250, self.bronze))
        coins.append(coin.Coin(245, 250, self.gold))
        coins.append(coin.Coin(544, 250, self.silver))
       
        # Row 4
        coins.append(coin.Coin(340, 325, self.gold))
        coins.append(coin.Coin(648, 325, self.bronze))

        # Row 5
        coins.append(coin.Coin(50, 420, self.gold))
        coins.append(coin.Coin(145, 420, self.gold)) 
        coins.append(coin.Coin(245, 420, self.silver))
        coins.append(coin.Coin(444, 420, self.gold)) 
        coins.append(coin.Coin(544, 420, self.gold))

        return coins        

    """
    Level 10 Coins
    """
    def level10(self):
        coins = []

        # Row 1
        coins.append(coin.Coin(215, 115, self.silver))
        coins.append(coin.Coin(390, 115, self.silver))
        coins.append(coin.Coin(565, 115, self.bronze))
        
        # Row 2
        coins.append(coin.Coin(120, 195, self.bronze))
        coins.append(coin.Coin(300, 195, self.silver))
        coins.append(coin.Coin(470, 195, self.gold))

        # Row 3
        coins.append(coin.Coin(40, 275, self.gold))
        coins.append(coin.Coin(180, 275, self.gold))
        coins.append(coin.Coin(350, 275, self.gold))
        coins.append(coin.Coin(565, 275, self.gold))
       
        # Row 4
        coins.append(coin.Coin(40, 355, self.gold))
        coins.append(coin.Coin(130, 355, self.gold))
        coins.append(coin.Coin(365, 355, self.gold))

        # Row 5
        coins.append(coin.Coin(40, 435, self.gold))
        coins.append(coin.Coin(240, 435, self.gold))

        return coins            

    """
    If a player has collected a coin, remove it from the screen and add 
    the coin's worth to the player's wealth
    """
    def player_has_reached(self, player, coins):
        for c in coins:
            if c.rectangle.colliderect(player.rectangle):
                player.add_to_wealth(c.value)
                coins.remove(c)