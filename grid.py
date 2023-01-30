from math import floor
import pygame
import globalInfo
gridSprite = globalInfo.ScaleSprite(pygame.image.load("Sprites/Grid/Grid.png"))
greenGridSprite = globalInfo.ScaleSprite(
    pygame.image.load("Sprites/Grid/Grid-Green.png"))
redGridSprite = globalInfo.ScaleSprite(
    pygame.image.load("Sprites/Grid/Grid-Red.png"))
blueGridSprite = globalInfo.ScaleSprite(
    pygame.image.load("Sprites/Grid/Grid-Blue.png"))

cellColors = {"Green": greenGridSprite,
              "Red": redGridSprite, "Blue": blueGridSprite}


class CellInfo():
    def __init__(self, position: tuple[int, int], color: str) -> None:
        self.color = color
        self.position = position


cellsToAddNext: list[CellInfo] = []


def AddColoredCell(clampedPosition: tuple[int, int], color: str):
    global cellsToAddNext
    cellsToAddNext.append(CellInfo(clampedPosition, color))


def BlitGrid(screen: pygame.surface.Surface) -> None:
    global cellsToAddNext

    sprite = globalInfo.ScaleSprite(gridSprite)
    size: tuple = (sprite.get_width(), sprite.get_height())
    for i in range(50):
        for j in range(25):
            screen.blit(sprite, (i * size[0], j * size[1]))

    for cell in cellsToAddNext:
        screen.blit(cellColors[cell.color], cell.position)
    cellsToAddNext = []


def ClampToGrid(coordinates: tuple[int, int]) -> tuple[int, int]:
    return (floor(coordinates[0] / globalInfo.gridSize) * globalInfo.gridSize,
            floor(coordinates[1] / globalInfo.gridSize) * globalInfo.gridSize)
