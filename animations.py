import pygame
import math


class Animation():
    advancement: float = 0
    currentFrame: int = 0

    def __init__(self, frames: list[pygame.surface.Surface], loop: bool, length: float):
        self.frames = frames + [frames[-1]]
        self.loop = loop
        self.length = length

    def Update(self, framerate: int):

        if self.loop and self.advancement == .999:
            self.advancement = 0

        self.advancement += 1 / framerate / self.length
        self.advancement = min(self.advancement, .999)

        self.currentFrame = math.floor(
            (len(self.frames) - 1) * self.advancement)

    def CurrentAnimSprite(self):
        return self.frames[self.currentFrame]
