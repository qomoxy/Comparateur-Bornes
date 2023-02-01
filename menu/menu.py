import pygame
from pygame.locals import *
from button import Button
from Base.actions import Action
import menu.menu

pygame.init()


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def mainMenu() -> None:
    window = pygame.display.set_mode((0, 0), RESIZABLE)
    BackGround = Background('sprites/menu/background_menu.png', [0, 0])

    runing = True
    while runing:
        mousePose = pygame.mouse.get_pos()

        window.blit(pygame.transform.scale(
            BackGround.image, (window.get_width(), window.get_height())), (0, 0))

        startButton = Button(
            0, 0, 'sprites/menu/startButton.png', 1, Action(menu.menu, 'StartGame'))

        if startButton.draw(window):
            pass

        for event in pygame.event.get():
            if event.type == QUIT:
                runing = False

        pygame.display.update()

    pygame.quit()


mainMenu()


def StartGame():
    print("StartGame")
