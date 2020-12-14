import pygame
import barrier

class BarrierManager:

    """
    Constructor
    """
    def __init__(self):
        pass
        
    """
    Place the barriers on the screen
    """
    def draw(self, screen, barriers):
        for b in barriers:
            pygame.draw.rect(screen, b.colour, b.rectangle)

    """
    Level 1 Barriers
    """
    def level1(self):
        barriers = []
        barriers.append(barrier.Barrier(0, 70, 600, 10)) # 1
        barriers.append(barrier.Barrier(0, 145, 420, 10)) # 2
        barriers.append(barrier.Barrier(520, 145, 550, 10)) # 3
        barriers.append(barrier.Barrier(0, 225, 550, 10)) # 4
        barriers.append(barrier.Barrier(0, 305, 250, 10)) # 5 
        barriers.append(barrier.Barrier(350, 305, 250, 10)) # 6
        barriers.append(barrier.Barrier(475, 315, 10, 70)) # 7
        barriers.append(barrier.Barrier(100, 385, 600, 10)) # 8
        return barriers

    """
    Level 2 Barriers
    """
    def level2(self):
        barriers = []
        barriers.append(barrier.Barrier(105, 110, 305, 10)) # 1
        barriers.append(barrier.Barrier(410, 70, 200, 10)) # 2
        barriers.append(barrier.Barrier(410, 80, 10, 110)) # 3
        barriers.append(barrier.Barrier(600, 80, 10, 200)) # 4
        barriers.append(barrier.Barrier(105, 190, 315, 10)) # 5
        barriers.append(barrier.Barrier(105, 200, 10, 200)) # 6
        barriers.append(barrier.Barrier(205, 280, 10, 120)) # 7
        barriers.append(barrier.Barrier(205, 270, 215, 10)) # 8
        barriers.append(barrier.Barrier(410, 280, 10, 90)) # 9
        barriers.append(barrier.Barrier(420, 360, 90, 10)) # 10
        barriers.append(barrier.Barrier(460, 360, 10, 110)) # 11
        barriers.append(barrier.Barrier(510, 200, 10, 170)) # 12
        barriers.append(barrier.Barrier(520, 280, 90, 10)) # 13
        barriers.append(barrier.Barrier(610, 360, 90, 10)) # 14
        return barriers

    """
    Level 3 Barriers
    """
    def level3(self):
        barriers = []
        barriers.append(barrier.Barrier(90, 0, 10, 233)) # 1
        barriers.append(barrier.Barrier(180, 70, 10, 233)) # 2
        barriers.append(barrier.Barrier(90, 303, 100, 10)) # 3
        barriers.append(barrier.Barrier(90, 383, 190, 10)) # 4
        barriers.append(barrier.Barrier(270, 70, 10, 90)) # 5
        barriers.append(barrier.Barrier(360, 70, 210, 10)) # 6
        barriers.append(barrier.Barrier(280, 150, 280, 10)) # 7
        barriers.append(barrier.Barrier(560, 150, 10, 80)) # 8
        barriers.append(barrier.Barrier(560, 190, 140, 10)) # 9
        barriers.append(barrier.Barrier(280, 230, 290, 10)) # 10
        barriers.append(barrier.Barrier(270, 230, 10, 80)) # 11
        barriers.append(barrier.Barrier(360, 310, 10, 80)) # 12
        barriers.append(barrier.Barrier(370, 310, 330, 10)) # 13
        return barriers

    """
    Level 4 Barriers
    """
    def level4(self):
        barriers = []
        barriers.append(barrier.Barrier(0, 70, 155, 10)) # 1
        barriers.append(barrier.Barrier(250, 0, 10, 80)) # 2
        barriers.append(barrier.Barrier(260, 70, 140, 10)) # 3
        barriers.append(barrier.Barrier(390, 80, 10, 110)) # 4
        barriers.append(barrier.Barrier(490, 70, 210, 10)) # 5
        barriers.append(barrier.Barrier(0, 145, 250, 10)) # 6
        barriers.append(barrier.Barrier(85, 225, 220, 10)) # 7
        barriers.append(barrier.Barrier(85, 235, 10, 150)) # 8
        barriers.append(barrier.Barrier(95, 300, 300, 10)) # 9
        barriers.append(barrier.Barrier(95, 375, 500, 10)) # 10
        barriers.append(barrier.Barrier(485, 265, 10, 110)) # 11
        barriers.append(barrier.Barrier(485, 185, 110, 10)) # 12
        barriers.append(barrier.Barrier(585, 265, 10, 110)) # 13
        return barriers

    """
    Level 5 Barriers
    """
    def level5(self):
        barriers = []
        barriers.append(barrier.Barrier(0, 70, 300, 10)) # 1
        barriers.append(barrier.Barrier(400, 0, 10, 120)) # 2
        barriers.append(barrier.Barrier(500, 110, 110, 10)) # 3
        barriers.append(barrier.Barrier(600, 120, 10, 65)) # 4
        barriers.append(barrier.Barrier(90, 185, 520, 10)) # 5
        barriers.append(barrier.Barrier(435, 195, 10, 80)) # 6
        barriers.append(barrier.Barrier(90, 265, 250, 10)) # 7
        barriers.append(barrier.Barrier(150, 275, 10, 100)) # 8
        barriers.append(barrier.Barrier(90, 375, 310, 10)) # 9
        barriers.append(barrier.Barrier(190, 385, 10, 80)) # 10
        barriers.append(barrier.Barrier(535, 265, 65, 10)) # 11
        barriers.append(barrier.Barrier(600, 265, 10, 110)) # 12
        barriers.append(barrier.Barrier(500, 375, 110, 10)) # 13
        return barriers

    """
    Level 6 Barriers
    """
    def level6(self):
        barriers = []
        barriers.append(barrier.Barrier(80, 70, 195, 10)) # 1
        barriers.append(barrier.Barrier(80, 80, 10, 70)) # 2
        barriers.append(barrier.Barrier(80, 230, 10, 240)) # 3
        barriers.append(barrier.Barrier(170, 80, 10, 310)) # 4
        barriers.append(barrier.Barrier(170, 390, 155, 10)) # 5
        barriers.append(barrier.Barrier(365, 0, 10, 80)) # 6
        barriers.append(barrier.Barrier(300, 150, 310, 10)) # 7
        barriers.append(barrier.Barrier(600, 70, 10, 80)) # 8
        barriers.append(barrier.Barrier(290, 150, 10, 90)) # 9
        barriers.append(barrier.Barrier(290, 240, 220, 10)) # 10
        barriers.append(barrier.Barrier(290, 315, 310, 10)) # 11
        barriers.append(barrier.Barrier(600, 240, 10, 230)) # 12
        barriers.append(barrier.Barrier(450, 390, 150, 10)) # 13
        return barriers

    """
    Level 7 Barriers
    """
    def level7(self):
        barriers = []
        barriers.append(barrier.Barrier(80, 70, 10, 250)) # 1
        barriers.append(barrier.Barrier(90, 240, 100, 10)) # 2
        barriers.append(barrier.Barrier(190, 70, 10, 320)) # 3
        barriers.append(barrier.Barrier(80, 390, 540, 10)) # 4
        barriers.append(barrier.Barrier(285, 235, 10, 70)) # 5
        barriers.append(barrier.Barrier(285, 305, 420, 10)) # 6
        barriers.append(barrier.Barrier(285, 70, 10, 85)) # 7
        barriers.append(barrier.Barrier(285, 155, 155, 10)) # 8
        barriers.append(barrier.Barrier(440, 155, 10, 70)) # 9
        barriers.append(barrier.Barrier(375, 70, 195, 10)) # 10
        barriers.append(barrier.Barrier(570, 70, 10, 155)) # 11
        return barriers