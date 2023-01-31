import pygame
import math
from Base.globalInfo import ScaleSprite
from math import floor


class Animation():
    def __init__(self, spriteSheet: pygame.surface.Surface, loop: bool, length: float, frameCount: tuple[int, int] = (1, 1), onAnimationFinishAction=None) -> None:
        self.loop: bool = loop
        self.length: float = length
        self.frames: list[pygame.surface.Surface] = [
            self.getFrame(spriteSheet,
                          offset=(floor((i)/frameCount[0] * spriteSheet.get_width()),
                                  floor((j)/frameCount[1] * spriteSheet.get_height())),
                          size=(floor(spriteSheet.get_width()/frameCount[0]),
                                floor(spriteSheet.get_height()/frameCount[1])))
            for i in range(frameCount[0]) for j in range(frameCount[1])]
        self.frames.append(self.frames[-1])
        self.onAnimationFinishAction = onAnimationFinishAction

    def getFrame(self, spriteSheet: pygame.surface.Surface, size: tuple[int, int], offset: tuple[int, int]):
        print(f"{size}    {offset}")
        frame = pygame.surface.Surface(
            size, pygame.SRCALPHA, 32).convert_alpha()
        frame.blit(spriteSheet, (0, 0),
                   (offset[0], offset[1], size[0], size[1]))
        return ScaleSprite(frame)


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
                if self.anim.onAnimationFinishAction != None:
                    self.anim.onAnimationFinishAction.Invoke()

        self.advancement += 1 / framerate / self.anim.length
        self.advancement = min(self.advancement, .999)

        self.currentFrame = math.floor(
            (len(self.anim.frames) - 1) * self.advancement)

    def IsAnimationDone(self) -> bool:
        return not self.anim.loop and self.advancement == .999

    def CurrentAnimSprite(self):
        return self.anim.frames[self.currentFrame]
