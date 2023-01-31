
import random
import pygame

gridSize = 64


def ScaleSprite(sprite: pygame.surface.Surface):
    return pygame.transform.scale(sprite, (gridSize, gridSize))


def TupleToRandom(tuple: tuple[int, int]):
    return random.randint(tuple[0], tuple[1])
