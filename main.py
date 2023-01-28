import pygame as pygame
import events
import player

pygame.init()

pygame.display.set_mode((200, 200))  # , pygame.FULLSCREEN)
pygame.display.set_caption("Jeu de role")


framerate: int = 60
running: bool = True

clock = pygame.time.Clock()

player = player.Player()

print("\n\n\nclass events: quitter le jeu, deplacer le joueur, utiliser une attaque etc\nclass joueur: mouvement du joueur (Fleches), vie etc\n SVP separez le code en plusieurs morceaux\n\n\n")

while running:
    events.HandleEvents()
    pygame.display.update()
    player.Update(framerate)
    clock.tick(framerate)


pygame.quit()

if __name__ != "__main__":
    print("n'importez pas ce script")
