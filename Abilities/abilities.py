import pygame
from Entities.entity import Entity
from Base.globalInfo import TupleToRandom
from Abilities.abilityEffects import EffectManager
import grid


class Ability():
    def __init__(self, speed: tuple[int, int], name: str, info: str, abilityEffects: EffectManager, cellColor: str = "Red", shape: list[str] = ["•••",
                                                                                                                                                "•P•",
                                                                                                                                                "•••"]) -> None:
        self.name: str = name
        self.info: str = info
        self.baseSpeed: tuple[int, int] = speed
        self.speed: int = TupleToRandom(speed)
        self.shape = shape
        self.cellColor = cellColor
        self.abilityEffects: EffectManager = abilityEffects
