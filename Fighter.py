import pygame


class Fighter():
    def __init__(self, x, y) -> None:
        self.rect = pygame.Rect((x, y), 80, 180)
        
    def draw(self, surface)