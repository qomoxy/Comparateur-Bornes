import pygame as pygame
import Base.animations as animations
from Abilities.abilities import Ability
from Entities.Player.player import Player
from Entities.entity import Entity
from Entities.Enemies.enemy import Enemy
from Abilities.abilityEffects import EffectManager, Effect
import Base.events as events
import Base.actions as actions
import grid

pygame.init()

screen = pygame.display.set_mode((64*16, 64*9))  # , pygame.FULLSCREEN)
pygame.display.set_caption("Jeu de rôle")


framerate: int = 60
running: bool = True

clock = pygame.time.Clock()

slimeIdleAnim = animations.Animation(
    spriteSheet=pygame.image.load("Sprites/slime.png"),
    loop=True, length=.6,
    sheetSpriteCount=(12, 1), spriteAnchor=(0, .5),
    startEndFrames=(0, 1))

enemy = Enemy(entity=Entity(3, (128, 128), "Slime", "Un slime",
                            [Ability((5, 10), "Saut", "Boing !",
                                     EffectManager(
                                [Effect(damage=(2, 4))]), shape=["•X•",
                                                                 "XPX",
                                                                 "•X•"])]),
              idleAnimation=slimeIdleAnim)

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
