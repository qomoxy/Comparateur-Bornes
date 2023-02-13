import pygame as pygame
from Entities.Player.player import Player
from Entities.Enemies.enemy import Enemy
import Entities.Enemies.enemyList as enemies
import Base.events as events
import grid

pygame.init()

screen = pygame.display.set_mode((64*16, 64*9))  # , pygame.FULLSCREEN)
pygame.display.set_caption("Jeu de rôle")


framerate: int = 60
running: bool = True

clock = pygame.time.Clock()

enemy = Enemy(enemies.slimeEnemyProperties)

player = Player()

print("\n\n\nclass events: quitter le jeu, deplacer le joueur, utiliser une attaque etc\nclass joueur: mouvement du joueur (Fleches), vie etc\nclass animations: creer une animation\n SVP separez le code en plusieurs morceaux\n\n\n")

while running:
    events.HandleEvents()

    screen.fill((62, 137, 72))
    grid.BlitGrid(screen)

    enemy.Update(framerate)
    enemy.animator.Blit(
        screen, enemy.entity.rect.topleft)

    player.Update(framerate)
    player.pAnims.playerAnimator.Blit(
        screen, player.pEntity.rect.topleft)

    pygame.display.flip()
    clock.tick(framerate)


pygame.quit()

if __name__ != "__main__":
    print("n'importez pas ce script")
