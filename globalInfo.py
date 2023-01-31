
import pygame

gridSize = 64


def ScaleSprite(sprite: pygame.surface.Surface):
    return pygame.transform.scale(sprite, (gridSize, gridSize))
