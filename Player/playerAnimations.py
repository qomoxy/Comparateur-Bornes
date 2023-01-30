import pygame
import animations


class PlayerAnimation():
    currentMoveCooldown: float = 0
    moveCooldown: float = .3
    rect = pygame.Rect(0, 0, 10, 10)

    idleAnim = animations.Animation([pygame.image.load("Sprites/test1.png"),
                                     pygame.image.load("Sprites/test2.png")], True, 1)

    walkAnim = animations.Animation([pygame.image.load("Sprites/test1.png"),
                                     pygame.image.load("Sprites/test2.png")], True, 1)

    def __init__(self):
        self.playerAnimator = animations.Animator()
        self.playerAnimator.SetAnimation(self.idleAnim)

    def UpdateAnimations(self, framerate: int):
        self.playerAnimator.Update(framerate)

    def SetAnimation(self, animation: animations.Animation):
        self.playerAnimator.SetAnimation(animation)

    def Blit(self, screen: pygame.surface.Surface, position: tuple):
        screen.blit(self.playerAnimator.CurrentAnimSprite(),
                    position)
