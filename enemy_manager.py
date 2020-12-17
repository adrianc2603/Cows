import pygame
import enemy

class EnemyManager:

    """
    Constructor
    """
    def __init__(self, screen, player):
        self.blue_image = "resources/blue_enemy.png"
        self.red_image = "resources/red_enemy.png"
        self.screen = screen
        self.player = player

    """
    Place all enemies on the screen
    """
    def draw(self, enemies):
        for e in enemies:
            self.screen.blit(e.image, (e.x, e.y))

    """
    Level 3 Enemies
    """
    def level3(self):
        enemies = []
        enemies.append(enemy.Enemy(self.blue_image, 610, 20)) 
        return enemies

    """
    Level 4 Enemies
    """
    def level4(self):
        enemies = []
        enemies.append(enemy.Enemy(self.blue_image, 290, 5)) 
        enemies.append(enemy.Enemy(self.blue_image, 610, 5)) 
        enemies.append(enemy.Enemy(self.blue_image, 190, 160)) 
        enemies.append(enemy.Enemy(self.blue_image, 511, 205)) 
        enemies.append(enemy.Enemy(self.blue_image, 400, 305)) 
        enemies.append(enemy.Enemy(self.blue_image, 40, 395)) 
        return enemies

    """
    Level 5 Enemies
    """
    def level5(self):
        enemies = []
        enemies.append(enemy.Enemy(self.blue_image, 320, 20)) 
        enemies.append(enemy.Enemy(self.blue_image, 632, 40)) 
        enemies.append(enemy.Enemy(self.red_image, 460, 205, True)) 
        enemies.append(enemy.Enemy(self.blue_image, 270, 295)) 
        enemies.append(enemy.Enemy(self.blue_image, 320, 395)) 
        return enemies


    """
    Level 6 Enemies
    """
    def level6(self):
        enemies = []
        enemies.append(enemy.Enemy(self.blue_image, 200, 90)) 
        enemies.append(enemy.Enemy(self.blue_image, 520, 80)) 
        enemies.append(enemy.Enemy(self.red_image, 625, 80, True)) 
        return enemies

    """
    Level 7 Enemies
    """
    def level7(self):
        enemies = []
        enemies.append(enemy.Enemy(self.blue_image, 10, 10)) 
        enemies.append(enemy.Enemy(self.blue_image, 10, 90)) 
        enemies.append(enemy.Enemy(self.blue_image, 10, 170)) 
        enemies.append(enemy.Enemy(self.blue_image, 10, 250)) 
        enemies.append(enemy.Enemy(self.red_image, 213, 85, True)) 
        enemies.append(enemy.Enemy(self.red_image, 310, 85, True)) 
        return enemies

    """
    Level 8 Enemies
    """
    def level8(self):
        enemies = []
        enemies.append(enemy.Enemy(self.blue_image, 10, 20))
        enemies.append(enemy.Enemy(self.red_image, 180, 20, True))
        enemies.append(enemy.Enemy(self.blue_image, 270, 190))
        enemies.append(enemy.Enemy(self.blue_image, 520, 280))
        enemies.append(enemy.Enemy(self.blue_image, 520, 420))
        enemies.append(enemy.Enemy(self.red_image, 617, 420, True))
        return enemies

    """
    Level 9 Enemies
    """
    def level9(self):
        enemies = []
        enemies.append(enemy.Enemy(self.red_image, 15, 100, True))
        enemies.append(enemy.Enemy(self.blue_image, 18, 310))
        enemies.append(enemy.Enemy(self.red_image, 320, 395, True))
        return enemies

    """
    Level 10 Enemies
    """
    def level10(self):
        enemies = []
        enemies.append(enemy.Enemy(self.red_image, 12, 175, True))
        enemies.append(enemy.Enemy(self.blue_image, 205, 340))
        enemies.append(enemy.Enemy(self.red_image, 100, 410, True))
        enemies.append(enemy.Enemy(self.red_image, 330, 410, True))
        enemies.append(enemy.Enemy(self.blue_image, 440, 340))
        enemies.append(enemy.Enemy(self.red_image, 542, 340, True))
        enemies.append(enemy.Enemy(self.blue_image, 100, 20)) 
        enemies.append(enemy.Enemy(self.blue_image, 220, 20)) 
        enemies.append(enemy.Enemy(self.blue_image, 340, 20)) 
        enemies.append(enemy.Enemy(self.blue_image, 460, 20)) 
        enemies.append(enemy.Enemy(self.blue_image, 580, 20)) 
        enemies.append(enemy.Enemy(self.blue_image, 630, 100)) 
        enemies.append(enemy.Enemy(self.blue_image, 630, 200)) 
        enemies.append(enemy.Enemy(self.blue_image, 630, 300)) 
        enemies.append(enemy.Enemy(self.blue_image, 630, 400)) 
        return enemies    

    """
    If a player has collided with an enemy, remove it from the screen and 
    subtract wealth from the player
    """
    def player_has_reached(self, enemies):
        for e in enemies:
            if e.rectangle.colliderect(self.player.rectangle):
                self.player.remove_wealth(e)
                enemies.remove(e)
