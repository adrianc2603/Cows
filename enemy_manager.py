import pygame
import enemy

class EnemyManager:

    """
    Constructor
    """
    def __init__(self):
        self.blue_image = "resources/blue_enemy.png"
        self.red_image = "resources/red_enemy.png"

    """
    Place all enemies on the screen
    """
    def draw(self, screen, enemies):
        for e in enemies:
            screen.blit(e.image, (e.x, e.y))

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
        enemies.append(enemy.Enemy(self.red_image, 460, 205)) 
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
        enemies.append(enemy.Enemy(self.red_image, 625, 80)) 
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
        enemies.append(enemy.Enemy(self.red_image, 213, 85)) 
        enemies.append(enemy.Enemy(self.red_image, 310, 85)) 
        return enemies

    """
    If a player has collided with an enemy, remove it from the screen and 
    subtract wealth from the player
    """
    def player_has_reached(self, player, enemies, screen, screen_manager):
        for e in enemies:
            if e.rectangle.colliderect(player.rectangle):
                player.remove_wealth(e.image_path, screen, screen_manager)
                enemies.remove(e)