import pygame as pygame
from sys import exit

pygame.init()

pygame.display.set_mode((50, 50))  # , pygame.FULLSCREEN)
pygame.display.set_caption("Jeu de role")


def HandleEvents():
    for event in pygame.event.get():
        print(f"{event.type}   {pygame.QUIT}")
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


framerate: int = 60
running: bool = True

clock = pygame.time.Clock()

while running:
    HandleEvents()
    pygame.display.update()
    clock.tick(framerate)


pygame.quit()
