import pygame
from button import Button
from Base.actions import Action

pygame.init()


class Background:
    def __init__(self, image_file, location):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def mainMenu() -> None:
    window = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    BackGround = Background('background_menu.png', [0, 0])

    runing = True
    while runing:
        mousePose = pygame.mouse.get_pos()

        window.blit(pygame.transform.scale(
            BackGround.image, (window.get_width(), window.get_height())), (0, 0))

        startButton = Button(
            0, 0, 'startButton.png', 1, Action(ref_StartGame, 'StartGame'))

        if startButton.draw(window):
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        pygame.display.update()

    pygame.quit()


def StartGame():
    print("StartGame")
