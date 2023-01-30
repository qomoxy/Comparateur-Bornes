import pygame
import math
from globalInfo import ScaleSprite


class Animation():

    def __init__(self, frames: list[pygame.surface.Surface], loop: bool, length: float) -> None:
        self.loop: bool = loop
        self.length: float = length
        self.frames: list[pygame.surface.Surface] = RescaleFrames(
            frames + [frames[-1]])


class Animator():
    advancement: float = 0
    currentFrame: int = 0

    def SetAnimation(self, anim: Animation) -> None:
        self.anim = anim
        self.advancement = 0

    def Update(self, framerate: int) -> None:

        if self.anim.loop and self.advancement == .999:
            self.advancement = 0

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
