
import random
import pygame

gridSize = 64


def ScaleSprite(sprite: pygame.surface.Surface):
    ratioYoverX = sprite.get_height() / sprite.get_width()
    return pygame.transform.scale(sprite, (gridSize, ratioYoverX * gridSize))


def TupleToRandom(tuple: tuple[int, int]):
    return random.randint(tuple[0], tuple[1])
