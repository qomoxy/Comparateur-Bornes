import pygame as pygame
import events
import player

pygame.init()

screen = pygame.display.set_mode((600, 600))  # , pygame.FULLSCREEN)
pygame.display.set_caption("Jeu de role")


framerate: int = 60
running: bool = True

clock = pygame.time.Clock()

player = player.Player([pygame.image.load("test1.png"),
                       pygame.image.load("test2.png")])

print("\n\n\nclass events: quitter le jeu, deplacer le joueur, utiliser une attaque etc\nclass joueur: mouvement du joueur (Fleches), vie etc\nclass animations: creer une animation\n SVP separez le code en plusieurs morceaux\n\n\n")

while running:
    events.HandleEvents()

    screen.fill((0, 0, 0))

    player.Update(framerate)
    player.Blit(screen)

    pygame.display.flip()
    clock.tick(framerate)


pygame.quit()

if __name__ != "__main__":
    print("n'importez pas ce script")
