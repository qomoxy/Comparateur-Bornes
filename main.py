import pygame as pygame
import events

pygame.init()

pygame.display.set_mode((200, 200))  # , pygame.FULLSCREEN)
pygame.display.set_caption("Jeu de role")


framerate: int = 60
running: bool = True

clock = pygame.time.Clock()

while running:
    events.HandleEvents()
    pygame.display.update()
    clock.tick(framerate)


pygame.quit()
