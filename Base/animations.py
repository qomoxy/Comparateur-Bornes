import pygame
import math
from Base.globalInfo import ScaleSprite
from Base.actions import Action


class Animation():

    def __init__(self, frames: list[pygame.surface.Surface], loop: bool, length: float, onAnimationFinish=None) -> None:
        self.loop: bool = loop
        self.length: float = length
        self.frames: list[pygame.surface.Surface] = RescaleFrames(
            frames + [frames[-1]])
        self.onAnimationFinish = onAnimationFinish


class Animator():
    advancement: float = 0
    currentFrame: int = 0
    animationFinished: bool = False

    def SetAnimation(self, anim: Animation) -> None:
        self.anim = anim
        self.advancement = 0
        self.animationFinished = False

    def Update(self, framerate: int) -> None:
        if self.animationFinished:
            return

        if self.advancement == .999:
            if self.anim.loop:
                self.advancement = 0
            else:
                self.animationFinished = True
                if self.anim.onAnimationFinish != None:
                    self.anim.onAnimationFinish.Invoke()

        self.advancement += 1 / framerate / self.anim.length
        self.advancement = min(self.advancement, .999)

        self.currentFrame = math.floor(
            (len(self.anim.frames) - 1) * self.advancement)

    def IsAnimationDone(self) -> bool:
        return not self.anim.loop and self.advancement == .999

    def CurrentAnimSprite(self):
        return self.anim.frames[self.currentFrame]


def RescaleFrames(frames: list[pygame.surface.Surface]):
    return [
        ScaleSprite(frame) for frame in frames]
