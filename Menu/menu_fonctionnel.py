import pygame
from pygame.locals import *
pygame.init()


width, height = 64*16, 64*9


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def mainMenu():
    window = pygame.display.set_mode((width, height), RESIZABLE)
    BackGround = Background('sprites/background_menu.png', [0, 0])

    runing = True
    while runing:
        mousePose = pygame.mouse.get_pos()

        window.blit(pygame.transform.scale(
            BackGround.image, (width, height)), (0, 0))
        window.blit(BackGround.image, BackGround.rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                runing = False

        pygame.display.update()

    pygame.quit()


mainMenu()
