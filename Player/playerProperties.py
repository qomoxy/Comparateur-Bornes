import pygame


class PlayerProperties():

    def __init__(self, health=20) -> None:
        self.health = health
        self.rect = pygame.Rect(0, 0, 10, 10)
