import pygame
import math
from Base.globalInfo import ScaleSprite
from math import floor


class Animation():
    def __init__(self, spriteSheet: pygame.surface.Surface,
                 loop: bool, length: float, sheetSpriteCount: tuple[int, int] = (1, 1),
                 startEndFrames: tuple[int, int] = (0, 0), spriteAnchor: tuple[float, float] = (0, 0),
                 onAnimationFinishAction=None) -> None:
        self.loop: bool = loop
        self.length: float = length
        self.spriteAnchor: tuple[float, float] = spriteAnchor

        self.frames: list[pygame.surface.Surface] = self.AddFrames(
            spriteSheet, sheetSpriteCount, startEndFrames)

        self.frames.append(self.frames[-1])
        self.onAnimationFinishAction = onAnimationFinishAction

    def AddFrames(self, spriteSheet: pygame.surface.Surface, sheetSpriteCount: tuple[int, int], startEndFrames: tuple[int, int]) -> list[pygame.surface.Surface]:
        frames: list[pygame.surface.Surface] = []

        startIndices: tuple[int, int] = self.GetIndicesOnSheetByCount(
            sheetSpriteCount, startEndFrames[0])

        # get las frame
        if startEndFrames[1] == 0:
            endIndices: tuple[int, int] = (
                sheetSpriteCount[1] - 1, sheetSpriteCount[0] - 1)
        else:
            endIndices: tuple[int, int] = self.GetIndicesOnSheetByCount(
                sheetSpriteCount, startEndFrames[1])

        # j = x axis (horizontal), i = y axis (vertical)
        for i in range(startIndices[1], endIndices[1] + 1):
            for j in range(startIndices[0], endIndices[0] + 1):
                hSize = floor(spriteSheet.get_width() /
                              sheetSpriteCount[0])
                vSize = floor(spriteSheet.get_height() /
                              sheetSpriteCount[1])
                hOffset = floor(i / sheetSpriteCount[0] *
                                spriteSheet.get_width())

                vOffset = floor(j / sheetSpriteCount[1] *
                                spriteSheet.get_height())
                frames.append(self.GetFrame(
                    spriteSheet=spriteSheet,
                    offset=(hOffset, vOffset),
                    size=(hSize, vSize)
                ))
        return frames

    def GetFrame(self, spriteSheet: pygame.surface.Surface, size: tuple[int, int], offset: tuple[int, int]):
        return ScaleSprite(spriteSheet.subsurface(pygame.rect.Rect(offset[0], offset[1], size[0], size[1])))

    def GetIndicesOnSheetByCount(self, sheetSize: tuple[int, int], frameCount: int) -> tuple[int, int]:
        i: int = floor(frameCount/sheetSize[0])
        j: int = frameCount - i * sheetSize[0]
        return (i, j)


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

    def Blit(self, screen: pygame.surface.Surface, position: tuple):
        xPos = position[0] - self.anim.spriteAnchor[0] * \
            self.anim.frames[0].get_width()
        yPos = position[1] - self.anim.spriteAnchor[1] * \
            self.anim.frames[0].get_height()
        screen.blit(self.CurrentAnimSprite(), (xPos, yPos))

    def CurrentAnimSprite(self):
        return self.anim.frames[self.currentFrame]
