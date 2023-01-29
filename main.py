import pygame as pygame
from Player.player import Player
from Player.playerAnimations import PlayerAnimation
from Player.playerClass import PlayerClass
from Player.playerMovement import PlayerMovement
from animations import Animation
import events

pygame.init()

screen = pygame.display.set_mode((600, 600))  # , pygame.FULLSCREEN)
pygame.display.set_caption("Jeu de rôle")


framerate: int = 60
running: bool = True

clock = pygame.time.Clock()

playerIdleAnim = Animation([pygame.image.load("test1.png"),
                            pygame.image.load("test2.png")], True, 1)
playerWalkAnim = Animation([pygame.image.load("test1.png"),
                            pygame.image.load("test2.png")], True, .1)

pClass = PlayerClass("Player", "Mage", "")
pMovement = PlayerMovement()
pAnimations = PlayerAnimation(playerIdleAnim, playerWalkAnim)

player = Player(pClass, pMovement, pAnimations)

print("\n\n\nclass events: quitter le jeu, deplacer le joueur, utiliser une attaque etc\nclass joueur: mouvement du joueur (Fleches), vie etc\nclass animations: creer une animation\n SVP separez le code en plusieurs morceaux\n\n\n")

while running:
    events.HandleEvents()

    screen.fill((0, 0, 0))

    player.Update(framerate)
    player.pAnims.Blit(screen, (player.pMovement.rect.x *
                       50, player.pMovement.rect.y * 50))

    pygame.display.flip()
    clock.tick(framerate)


pygame.quit()

if __name__ != "__main__":
    print("n'importez pas ce script")
