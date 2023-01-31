import pygame as pygame
from Abilities.abilities import Ability
from Entities.Player.player import Player
from Entities.entity import Entity
from Entities.Enemies.enemy import Enemy
from Abilities.abilityEffects import EffectManager, Effect
import Base.events
import grid

pygame.init()

screen = pygame.display.set_mode((64*16, 64*9))  # , pygame.FULLSCREEN)
pygame.display.set_caption("Jeu de rôle")


framerate: int = 60
running: bool = True

clock = pygame.time.Clock()

enemy = Enemy(Entity(3, (128, 128), "Slime", "Un slime", [
              Ability((5, 10), "Saut", "Boing !", EffectManager([Effect(damage=(2, 4))]), shape=["•X•",
                                                                                                 "XPX",
                                                                                                 "•X•"])]))
player = Player()

print("\n\n\nclass events: quitter le jeu, deplacer le joueur, utiliser une attaque etc\nclass joueur: mouvement du joueur (Fleches), vie etc\nclass animations: creer une animation\n SVP separez le code en plusieurs morceaux\n\n\n")

while running:
    Base.events.HandleEvents()

    screen.fill((62, 137, 72))
    grid.BlitGrid(screen)

    enemy.Update()

    player.Update(framerate)
    player.pAnims.Blit(
        screen, (player.pEntity.rect.x, player.pEntity.rect.y))

    pygame.display.flip()
    clock.tick(framerate)


pygame.quit()

if __name__ != "__main__":
    print("n'importez pas ce script")
