class LevelManager:

    """
    Constructor
    """
    def __init__(self):
        pass

    """
    Set the position of the player and grass at the beginning of each level.
    Display the warning messages for enemies when necessary 
    """
    def setup_level(self, level, player, grass, screen_manager, screen):
        if level == 1:
            player.level1()
            grass.level1()
            
        if level == 2:
            player.level2()
            grass.level2()

        if level == 3:
            screen_manager.blue_enemy_warning(screen)
            player.level3()
            grass.level3()

        if level == 4:
            player.level4()
            grass.level4()

        if level == 5:
            screen_manager.red_enemy_warning(screen)
            player.level5()
            grass.level5()

        if level == 6:
            player.level6()
            grass.level6()

        if level == 7:
            player.level7()
            grass.level7()

        if level == 8:
            player.level8()
            grass.level8()

        if level == 9:
            player.level9()
            grass.level9()

        if level == 10:
            player.level10()
            grass.level10()    

    """
    Return the list of barriers for each level level 
    """
    def get_level_barriers(self, level, barrier_manager):
        if level == 1:
            return barrier_manager.level1()

        if level == 2:
            return barrier_manager.level2()
        
        if level == 3:
            return barrier_manager.level3()

        if level == 4:
            return barrier_manager.level4()

        if level == 5:
            return barrier_manager.level5()

        if level == 6:
            return barrier_manager.level6()

        if level == 7:
            return barrier_manager.level7()

        if level == 8:
            return barrier_manager.level8()

        if level == 9:
            return barrier_manager.level9()

        if level == 10:
            return barrier_manager.level10()    

        return []

    """
    Return the list of coins for each level level 
    """
    def get_level_coins(self, level, coin_manager):
        if level == 1:
            return coin_manager.level1()

        if level == 2:
            return coin_manager.level2()
        
        if level == 3:
            return coin_manager.level3()

        if level == 4:
            return coin_manager.level4()

        if level == 5:
            return coin_manager.level5()

        if level == 6:
            return coin_manager.level6()

        if level == 7:
            return coin_manager.level7()

        if level == 8:
            return coin_manager.level8()

        if level == 9:
            return coin_manager.level9()   

        if level == 10:
            return coin_manager.level10()        

        return []

    """
    Return the list of coins for each level level 
    """
    def get_level_enemies(self, level, enemy_manager):
        if level == 3:
            return enemy_manager.level3()

        if level == 4:
            return enemy_manager.level4()

        if level == 5:
            return enemy_manager.level5()

        if level == 6:
            return enemy_manager.level6()

        if level == 7:
            return enemy_manager.level7()

        if level == 8:
            return enemy_manager.level8()

        if level == 9:
            return enemy_manager.level9()

        if level == 10:
            return enemy_manager.level10()    

        return []
