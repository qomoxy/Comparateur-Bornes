import pygame

gridSize = 64
spriteScale = 2


def ScaleSprite(sprite: pygame.surface.Surface):
    return pygame.transform.scale(sprite, (gridSize, gridSize))
