import pygame
import events
import animations


class PlayerAnimation():
    currentMoveCooldown: float = 0
    moveCooldown: float = .3
    rect = pygame.Rect(0, 0, 10, 10)

    def __init__(self, idleAnim: animations.Animation, walkAnim: animations.Animation):
        self.idleAnim = idleAnim
        self.walkAnim = walkAnim
        self.playerAnimator = animations.Animator()
        self.playerAnimator.SetAnimation(idleAnim)

    def UpdateAnimations(self, framerate: int):
        self.playerAnimator.Update(framerate)

    def SetAnimation(self, animation: animations.Animation):
        self.playerAnimator.SetAnimation(animation)

    def Blit(self, screen: pygame.surface.Surface, position: tuple):
        screen.blit(self.playerAnimator.CurrentAnimSprite(),
                    position)
