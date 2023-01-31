import pygame
import Base.animations as animations
from Base.actions import Action


class PlayerAnimation():
    currentMoveCooldown: float = 0
    moveCooldown: float = .3
    rect = pygame.Rect(0, 0, 10, 10)

    def __init__(self):
        self.idleAnim = animations.Animation([pygame.image.load("Sprites/test1.png"),
                                              pygame.image.load("Sprites/test2.png")], False, 1, Action(self, "Test"))

        self.walkAnim = animations.Animation([pygame.image.load("Sprites/test1.png"),
                                              pygame.image.load("Sprites/test2.png")], True, 1, Action(self, "Test"))

        self.playerAnimator = animations.Animator()
        self.playerAnimator.SetAnimation(self.idleAnim)

    def UpdateAnimations(self, framerate: int):
        self.playerAnimator.Update(framerate)

    def Test(self):
        print("Animation Finished")

    def SetAnimation(self, animation: animations.Animation):
        self.playerAnimator.SetAnimation(animation)

    def Blit(self, screen: pygame.surface.Surface, position: tuple):
        screen.blit(self.playerAnimator.CurrentAnimSprite(),
                    position)
