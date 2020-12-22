import pygame
import barrier

class BarrierManager:

    """
    Constructor
    """
    def __init__(self, screen):
        self.screen = screen

    """
    Place the barriers on the screen
    """
    def draw(self, barriers):
        for b in barriers:
            pygame.draw.rect(self.screen, b.colour, b.rectangle)

    """
    Level 1 Barriers
    """
    def level1(self):
        barriers = []
        barriers.append(barrier.Barrier(0, 70, 600, 10)) 
        barriers.append(barrier.Barrier(0, 145, 420, 10)) 
        barriers.append(barrier.Barrier(520, 145, 550, 10)) 
        barriers.append(barrier.Barrier(0, 225, 550, 10)) 
        barriers.append(barrier.Barrier(0, 305, 250, 10))  
        barriers.append(barrier.Barrier(350, 305, 250, 10)) 
        barriers.append(barrier.Barrier(475, 315, 10, 70)) 
        barriers.append(barrier.Barrier(100, 385, 600, 10)) 
        return barriers

    """
    Level 2 Barriers
    """
    def level2(self):
        barriers = []
        barriers.append(barrier.Barrier(105, 110, 305, 10)) 
        barriers.append(barrier.Barrier(410, 70, 200, 10)) 
        barriers.append(barrier.Barrier(410, 80, 10, 110)) 
        barriers.append(barrier.Barrier(600, 80, 10, 200)) 
        barriers.append(barrier.Barrier(105, 190, 315, 10)) 
        barriers.append(barrier.Barrier(105, 200, 10, 200)) 
        barriers.append(barrier.Barrier(205, 280, 10, 120)) 
        barriers.append(barrier.Barrier(205, 270, 215, 10)) 
        barriers.append(barrier.Barrier(410, 280, 10, 90)) 
        barriers.append(barrier.Barrier(420, 360, 90, 10)) 
        barriers.append(barrier.Barrier(460, 360, 10, 110)) 
        barriers.append(barrier.Barrier(510, 200, 10, 170)) 
        barriers.append(barrier.Barrier(520, 280, 90, 10)) 
        barriers.append(barrier.Barrier(610, 360, 90, 10)) 
        return barriers

    """
    Level 3 Barriers
    """
    def level3(self):
        barriers = []
        barriers.append(barrier.Barrier(90, 0, 10, 233)) 
        barriers.append(barrier.Barrier(180, 70, 10, 233)) 
        barriers.append(barrier.Barrier(90, 303, 100, 10)) 
        barriers.append(barrier.Barrier(90, 383, 190, 10)) 
        barriers.append(barrier.Barrier(270, 70, 10, 90)) 
        barriers.append(barrier.Barrier(360, 70, 210, 10)) 
        barriers.append(barrier.Barrier(280, 150, 280, 10)) 
        barriers.append(barrier.Barrier(560, 150, 10, 80)) 
        barriers.append(barrier.Barrier(560, 190, 140, 10)) 
        barriers.append(barrier.Barrier(280, 230, 290, 10)) 
        barriers.append(barrier.Barrier(270, 230, 10, 80)) 
        barriers.append(barrier.Barrier(360, 310, 10, 80)) 
        barriers.append(barrier.Barrier(370, 310, 330, 10)) 
        return barriers

    """
    Level 4 Barriers
    """
    def level4(self):
        barriers = []
        barriers.append(barrier.Barrier(0, 70, 155, 10)) 
        barriers.append(barrier.Barrier(250, 0, 10, 80)) 
        barriers.append(barrier.Barrier(260, 70, 140, 10)) 
        barriers.append(barrier.Barrier(390, 80, 10, 110)) 
        barriers.append(barrier.Barrier(490, 70, 210, 10)) 
        barriers.append(barrier.Barrier(0, 145, 250, 10)) 
        barriers.append(barrier.Barrier(85, 225, 220, 10)) 
        barriers.append(barrier.Barrier(85, 235, 10, 150)) 
        barriers.append(barrier.Barrier(95, 300, 300, 10)) 
        barriers.append(barrier.Barrier(95, 375, 500, 10)) 
        barriers.append(barrier.Barrier(485, 265, 10, 110)) 
        barriers.append(barrier.Barrier(485, 185, 110, 10)) 
        barriers.append(barrier.Barrier(585, 265, 10, 110)) 
        return barriers

    """
    Level 5 Barriers
    """
    def level5(self):
        barriers = []
        barriers.append(barrier.Barrier(0, 70, 300, 10)) 
        barriers.append(barrier.Barrier(400, 0, 10, 120)) 
        barriers.append(barrier.Barrier(500, 110, 110, 10)) 
        barriers.append(barrier.Barrier(600, 120, 10, 65)) 
        barriers.append(barrier.Barrier(90, 185, 520, 10)) 
        barriers.append(barrier.Barrier(435, 195, 10, 80)) 
        barriers.append(barrier.Barrier(90, 265, 250, 10)) 
        barriers.append(barrier.Barrier(150, 275, 10, 100)) 
        barriers.append(barrier.Barrier(90, 375, 310, 10)) 
        barriers.append(barrier.Barrier(190, 385, 10, 80)) 
        barriers.append(barrier.Barrier(535, 265, 65, 10)) 
        barriers.append(barrier.Barrier(600, 265, 10, 110)) 
        barriers.append(barrier.Barrier(500, 375, 110, 10)) 
        return barriers

    """
    Level 6 Barriers
    """
    def level6(self):
        barriers = []
        barriers.append(barrier.Barrier(80, 70, 195, 10)) 
        barriers.append(barrier.Barrier(80, 80, 10, 70)) 
        barriers.append(barrier.Barrier(80, 230, 10, 240)) 
        barriers.append(barrier.Barrier(170, 80, 10, 310)) 
        barriers.append(barrier.Barrier(170, 390, 155, 10)) 
        barriers.append(barrier.Barrier(405, 0, 10, 80)) 
        barriers.append(barrier.Barrier(300, 150, 310, 10)) 
        barriers.append(barrier.Barrier(600, 70, 10, 80)) 
        barriers.append(barrier.Barrier(290, 150, 10, 90)) 
        barriers.append(barrier.Barrier(290, 240, 220, 10)) 
        barriers.append(barrier.Barrier(290, 315, 310, 10)) 
        barriers.append(barrier.Barrier(600, 240, 10, 230)) 
        barriers.append(barrier.Barrier(450, 390, 150, 10)) 
        return barriers

    """
    Level 7 Barriers
    """
    def level7(self):
        barriers = []
        barriers.append(barrier.Barrier(80, 70, 10, 250)) 
        barriers.append(barrier.Barrier(90, 240, 100, 10)) 
        barriers.append(barrier.Barrier(190, 70, 10, 320)) 
        barriers.append(barrier.Barrier(80, 390, 540, 10)) 
        barriers.append(barrier.Barrier(285, 235, 10, 70)) 
        barriers.append(barrier.Barrier(285, 305, 420, 10)) 
        barriers.append(barrier.Barrier(285, 70, 10, 85)) 
        barriers.append(barrier.Barrier(285, 155, 155, 10)) 
        barriers.append(barrier.Barrier(440, 155, 10, 70)) 
        barriers.append(barrier.Barrier(375, 70, 195, 10)) 
        barriers.append(barrier.Barrier(570, 70, 10, 155)) 
        return barriers

    """
    Level 8 Barriers
    """
    def level8(self):
        barriers = []
        barriers.append(barrier.Barrier(90, 160, 10, 225)) 
        barriers.append(barrier.Barrier(100, 240, 155, 10)) 
        barriers.append(barrier.Barrier(255, 80, 10, 80)) 
        barriers.append(barrier.Barrier(255, 160, 100, 10)) 
        barriers.append(barrier.Barrier(345, 90, 10, 70)) 
        barriers.append(barrier.Barrier(345, 80, 160, 10)) 
        barriers.append(barrier.Barrier(495, 90, 10, 70)) 
        barriers.append(barrier.Barrier(495, 160, 90, 10)) 
        barriers.append(barrier.Barrier(585, 160, 10, 170)) 
        barriers.append(barrier.Barrier(345, 240, 10, 230)) 
        barriers.append(barrier.Barrier(585, 410, 10, 60))
        barriers.append(barrier.Barrier(590, 80, 110, 10)) 
        return barriers    

    """
    Level 9 Barriers
    """
    def level9(self):
        barriers = []
        barriers.append(barrier.Barrier(90, 80, 10, 300)) 
        barriers.append(barrier.Barrier(190, 120, 10, 250)) 
        barriers.append(barrier.Barrier(190, 110, 400, 10)) 
        barriers.append(barrier.Barrier(590, 110, 10, 260)) 
        barriers.append(barrier.Barrier(590, 450, 10, 50)) 
        barriers.append(barrier.Barrier(390, 370, 10, 150)) 
        barriers.append(barrier.Barrier(290, 280, 100, 10)) 
        barriers.append(barrier.Barrier(290, 200, 10, 80)) 
        barriers.append(barrier.Barrier(300, 200, 200, 10)) 
        barriers.append(barrier.Barrier(490, 210, 10, 160)) 
        barriers.append(barrier.Barrier(300, 360, 190, 10)) 
        return barriers    

    """
    Level 10 Barriers
    """
    def level10(self):
        barriers = []
        barriers.append(barrier.Barrier(80, 70, 540, 10)) 
        barriers.append(barrier.Barrier(610, 80, 10, 315)) 
        barriers.append(barrier.Barrier(80, 150, 450, 10)) 
        barriers.append(barrier.Barrier(80, 160, 10, 80)) 
        barriers.append(barrier.Barrier(90, 230, 40, 10)) 
        barriers.append(barrier.Barrier(520, 160, 10, 80)) 
        barriers.append(barrier.Barrier(230, 230, 180, 10)) 
        barriers.append(barrier.Barrier(410, 230, 10, 90)) 
        barriers.append(barrier.Barrier(80, 310, 220, 10)) 
        barriers.append(barrier.Barrier(290, 320, 10, 80)) 
        barriers.append(barrier.Barrier(80, 400, 10, 70)) 
        barriers.append(barrier.Barrier(80, 390, 100, 10)) 
        barriers.append(barrier.Barrier(300, 390, 110, 10)) 
        barriers.append(barrier.Barrier(400, 400, 10, 70)) 
        barriers.append(barrier.Barrier(420, 310, 100, 10)) 
        barriers.append(barrier.Barrier(520, 310, 10, 80)) 
        return barriers        