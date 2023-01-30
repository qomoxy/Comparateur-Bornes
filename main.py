import pygame as pygame
from Player.player import Player
import events
import grid

pygame.init()

screen = pygame.display.set_mode((64*16, 64*9))  # , pygame.FULLSCREEN)
pygame.display.set_caption("Jeu de rôle")


framerate: int = 60
running: bool = True

clock = pygame.time.Clock()

player = Player()

print("\n\n\nclass events: quitter le jeu, deplacer le joueur, utiliser une attaque etc\nclass joueur: mouvement du joueur (Fleches), vie etc\nclass animations: creer une animation\n SVP separez le code en plusieurs morceaux\n\n\n")

while running:
    events.HandleEvents()

    screen.fill((62, 137, 72))
    grid.BlitGrid(screen)

    player.Update(framerate)
    player.pAnims.Blit(
        screen, (player.pProperties.rect.x, player.pProperties.rect.y))

    pygame.display.flip()
    clock.tick(framerate)


pygame.quit()

if __name__ != "__main__":
    print("n'importez pas ce script")
