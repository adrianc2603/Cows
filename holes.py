import pygame

class Holes:

    """
    Constructor
    """
    def __init__(self, BLACK, RED):
        self.black = BLACK
        self.red = RED
        self.radius = 30
        self.diameter = 60

    """
    Place all holes on the screen
    """
    def draw(self, screen, holes):
        for h in holes:

            # Black holes
            if h[2] == 1:
                pygame.draw.circle(screen, self.black, [h[0], h[1]], self.radius)

            # Red holes
            if h[2] == 2:
                pygame.draw.circle(screen, self.red, [h[0], h[1]], self.radius)

    """
    Level 3 Hole
    """
    def level3(self):
        holes = []
        holes.append([640, 50, 1])
        return holes

    """
    Level 4 Holes
    """
    def level4(self):
        holes = []
        holes.append([320, 35, 1])
        holes.append([640, 35, 1])
        holes.append([220, 190, 1])
        holes.append([541, 235, 1])
        holes.append([430, 335, 1])
        holes.append([70, 425, 1])
        return holes

    """
    Level 5 Holes
    """
    def level5(self):
        holes = []
        holes.append([350, 35, 1])
        holes.append([652, 70, 2])
        holes.append([490, 235, 2])
        holes.append([300, 325, 1])
        holes.append([350, 425, 1])
        return holes


    """
    Level 6 Holes
    """
    def level6(self):
        holes = []
        holes.append([230, 120, 1])
        holes.append([550, 110, 1])
        holes.append([655, 110, 2])
        return holes

    """
    Level 7 Holes
    """
    def level7(self):
        holes = []
        holes.append([40, 40, 1])
        holes.append([40, 120, 1])
        holes.append([40, 200, 1])
        holes.append([40, 280, 1])
        holes.append([243, 115, 2])
        holes.append([340, 115, 2])
        return holes

    """
    If a player has collided with a hole, remove it from the screen and 
    subtract wealth from the player
    """
    def player_has_reached(self, player, holes, screen, BLACK, BACKGROUND):
        for h in holes:
            h_rect = pygame.Rect(h[0] - self.radius, h[1] - self.radius, self.diameter, self.diameter)
            if h_rect.colliderect(player.rectangle):
                player.remove_wealth(h[2], screen, BLACK, BACKGROUND)
                holes.remove(h)
