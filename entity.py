import pygame
from abilities import Ability
from effects import EffectManager
from globalInfo import TupleToRandom


class Entity():
    def __init__(self, health: int, name: str, info: str, abilities: list[Ability] = [], baseSpeed: tuple[int, int] = (0, 3), baseDefense: tuple[int, int] = (0, 3), effectsToApply: EffectManager = EffectManager([])) -> None:
        self.health = health
        self.defense = TupleToRandom(baseDefense)
        self.baseSpeed = TupleToRandom(baseSpeed)
        self.name = name
        self.info = info
        self.effectsToApply: EffectManager = effectsToApply
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.abilities: list[Ability] = abilities
