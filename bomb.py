import pygame

class Bomb:
    def __init__(self, x, y, WIDTH, HEIGTH, image, SURFACE):
        self.SURFACE = SURFACE
        self.IMAGE = pygame.transform.scale(image, (WIDTH, HEIGTH))
        self.X = x
        self.Y = y
        
    def drawBombs(self):
        self.SURFACE.blit(self.IMAGE,(self.X,self.Y))
        