import pygame
from pygame.locals import *
from Base.actions import Action


class Button():
    def __init__(self, x: int, y: int, imageFolder: str, scale, actionOnClick: Action):
        self.imageLoad = pygame.image.load(imageFolder)
        self.width: int = self.imageLoad.get_width()
        self.height: int = self.imageLoad.get_height()
        self.scale: int = scale
        self.image = pygame.transform.scale(self.imageLoad, (int(
            self.width * self.scale), int(self.height * self.scale)))
        self.coordonnate: tuple[int, int] = (x, y)
        self.rect = self.image.get_rect()
        self.clicked: bool = False
        self.actionOnClick = actionOnClick

    def draw(self, surface) -> None:
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.actionOnClick.Invoke()
                print("True")

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.coordonnate))
