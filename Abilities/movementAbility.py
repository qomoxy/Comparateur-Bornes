''''
import pygame
import grid


def TryMoveToPosition(rectToMove: pygame.rect.Rect, unclampedPosition: tuple[int, int]):

      targetPos: tuple[int, int] = grid.ClampToGrid(unclampedPosition)

       for cellPosition in self.shapeCellPositions:
            if (cellPosition[0] + self.entity.rect.x, cellPosition[1] + self.entity.rect.y) == targetPos:
                break
        else:
            return

        print("Moving")

        self.entity.rect = pygame.Rect(
            targetPos[0], targetPos[1], self.entity.rect.width, self.entity.rect.height)'''
