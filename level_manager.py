class LevelManager:

    """
    Constructor
    """
    def __init__(self, player, grass, screen, screen_manager, barrier_manager, 
        coin_manager, enemy_manager):
            self.player = player 
            self.grass = grass 
            self.screen_manager = screen_manager
            self.barrier_manager = barrier_manager
            self.coin_manager = coin_manager
            self.enemy_manager = enemy_manager

    """
    Set the position of the player and grass at the beginning of each level.
    Display the warning messages for enemies when necessary 
    """
    def setup_level(self, level):
        if level == 1:
            self.player.level1()
            self.grass.level1()
            
        if level == 2:
            self.player.level2()
            self.grass.level2()

        if level == 3:
            self.screen_manager.blue_enemy_warning()
            self.player.level3()
            self.grass.level3()

        if level == 4:
            self.player.level4()
            self.grass.level4()

        if level == 5:
            self.screen_manager.red_enemy_warning()
            self.player.level5()
            self.grass.level5()

        if level == 6:
            self.player.level6()
            self.grass.level6()

        if level == 7:
            self.player.level7()
            self.grass.level7()

        if level == 8:
            self.player.level8()
            self.grass.level8()

        if level == 9:
            self.player.level9()
            self.grass.level9()

        if level == 10:
            self.player.level10()
            self.grass.level10()    

    """
    Return the list of barriers for each level
    """
    def get_level_barriers(self, level):
        if level == 1:
            return self.barrier_manager.level1()

        if level == 2:
            return self.barrier_manager.level2()
        
        if level == 3:
            return self.barrier_manager.level3()

        if level == 4:
            return self.barrier_manager.level4()

        if level == 5:
            return self.barrier_manager.level5()

        if level == 6:
            return self.barrier_manager.level6()

        if level == 7:
            return self.barrier_manager.level7()

        if level == 8:
            return self.barrier_manager.level8()

        if level == 9:
            return self.barrier_manager.level9()

        if level == 10:
            return self.barrier_manager.level10()    

        return []

    """
    Return the list of coins for each level 
    """
    def get_level_coins(self, level):
        if level == 1:
            return self.coin_manager.level1()

        if level == 2:
            return self.coin_manager.level2()
        
        if level == 3:
            return self.coin_manager.level3()

        if level == 4:
            return self.coin_manager.level4()

        if level == 5:
            return self.coin_manager.level5()

        if level == 6:
            return self.coin_manager.level6()

        if level == 7:
            return self.coin_manager.level7()

        if level == 8:
            return self.coin_manager.level8()

        if level == 9:
            return self.coin_manager.level9()   

        if level == 10:
            return self.coin_manager.level10()        

        return []

    """
    Return the list of enemies for each level 
    """
    def get_level_enemies(self, level):
        if level == 3:
            return self.enemy_manager.level3()

        if level == 4:
            return self.enemy_manager.level4()

        if level == 5:
            return self.enemy_manager.level5()

        if level == 6:
            return self.enemy_manager.level6()

        if level == 7:
            return self.enemy_manager.level7()

        if level == 8:
            return self.enemy_manager.level8()

        if level == 9:
            return self.enemy_manager.level9()

        if level == 10:
            return self.enemy_manager.level10()    

        return []
