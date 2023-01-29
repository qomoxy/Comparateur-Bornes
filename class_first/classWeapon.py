import random
import pygame
from effects import EffectManager


class Weapon():
    def __init__(self, minDamage: int, maxDamage: int, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.damage = random.randint(minDamage, maxDamage)
        self.speed = 1
        self.weaponEffect: list[EffectManager] = []
        self.shape = ["000",
                      "000",
                      "000"]


class MeleeWeapon(Weapon):

    def __init__(self, minDamage: int, maxDamage: int, name: str, description: str) -> None:
        super().__init__(minDamage, maxDamage, name, description)
        self.shape = ["000",
                      "000",
                      "0X0"]


class RangedWeapon(Weapon):
    def __init__(self, minDamage: int, maxDamage: int, name: str, description: str) -> None:
        super().__init__(minDamage, maxDamage, name, description)
        self.range = 5
        self.shape = ["000",
                      "0X0",
                      "XXX"]


class DistanceWeapon(Weapon):
    def __init__(self, minDamage: int, maxDamage: int, name: str, description: str) -> None:
        super().__init__(minDamage, maxDamage, name, description)
        self.range = 6
        self.shape = ["0X0",
                      "000",
                      "000"]
