import pygame
import math


class Animation():
    def __init__(self, frames: list[pygame.surface.Surface], loop: bool, length: float):
        self.loop: bool = loop
        self.length: float = length
        self.frames: list[pygame.surface.Surface] = frames + [frames[-1]]


class Animator():
    advancement: float = 0
    currentFrame: int = 0

    def SetAnimation(self, anim: Animation):
        self.anim = anim
        self.advancement = 0

    def Update(self, framerate: int):

        if self.anim.loop and self.advancement == .999:
            self.advancement = 0

        self.advancement += 1 / framerate / self.anim.length
        self.advancement = min(self.advancement, .999)

        self.currentFrame = math.floor(
            (len(self.anim.frames) - 1) * self.advancement)

    def IsAnimationDone(self):
        return not self.anim.loop and self.advancement == .999

    def CurrentAnimSprite(self):
        return self.anim.frames[self.currentFrame]
