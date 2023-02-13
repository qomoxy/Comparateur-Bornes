import pygame
from Abilities.abilities import Ability
from Abilities.abilityEffects import EffectManager
from Base.globalInfo import TupleToRandom


class Entity():
    def __init__(self, health: int, name: str, info: str, startPosition: tuple[int, int], abilities: list[Ability] = [], baseSpeed: tuple[int, int] = (0, 3), baseDefense: tuple[int, int] = (0, 3), effectsToApply: EffectManager = EffectManager([])) -> None:
        self.health = health
        self.defense = TupleToRandom(baseDefense)
        self.speed = TupleToRandom(baseSpeed)
        self.name = name
        self.info = info
        self.effectsToApply: EffectManager = effectsToApply
        self.rect = pygame.Rect(startPosition[0], startPosition[1], 32, 32)
        self.abilities = abilities
