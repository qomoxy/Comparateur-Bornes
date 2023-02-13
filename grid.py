from math import floor
import pygame
import Base.globalInfo as globalInfo

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


def AddCell(cell: CellInfo):
    global cellsToAddNext
    cellsToAddNext.append(cell)


def AddCells(cells: list[CellInfo]):
    global cellsToAddNext
    for cell in cells:
        cellsToAddNext.append(cell)


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

# Pour les formes, utilisez "⬜" pour une cellule, "⬛" pour le centre de la forme, "🔲" pour le centre rempli de la forme et "⬜" pour l'espace vide


def ShapeToPositions(shape: list[str], offset: tuple[int, int] = (0, 0)) -> list[tuple[int, int]]:
    center: tuple[int, int] = (0, 0)
    positions: list[tuple[int, int]] = []

    for i in range(len(shape)):
        for j in range(len(shape[i])):
            value = shape[i][j]
            if value == "⬛" or value == "🔲":
                center = (i * globalInfo.gridSize, j * globalInfo.gridSize)
            if value in ["⬜", "🔲"]:
                positions.append(
                    (j * globalInfo.gridSize + offset[0], i * globalInfo.gridSize + offset[1]))

    if center != (0, 0):
        for i in range(len(positions)):
            positions[i] = (positions[i][0] - center[0],
                            positions[i][1] - center[1])

    return positions


def PositionsToCells(positions: list[tuple[int, int]], color: str):
    return [CellInfo(position, color)
            for position in positions]
