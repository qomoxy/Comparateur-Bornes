import random
import pygame
from Base.globalInfo import TupleToRandom


class Effect():
    def __init__(self, damage: tuple[int, int] = (2, 4), healing: tuple[int, int] = (0, 0), timesToApply: tuple[int, int] = (1, 1), probabilityToApply: float = .9) -> None:
        self.damage: int = TupleToRandom(damage)
        self.healing: int = TupleToRandom(healing)
        self.timesToApply: int = TupleToRandom(timesToApply)
        self.probabilityToApply: float = probabilityToApply

    def ApplyEffect(self):
        apply: bool = random.randint(1, 100) <= self.probabilityToApply * 100
        if apply:
            self.timesToApply -= 1

        # Appliquer ici l'effet
        print("Effet applique")

        return self.timesToApply <= 0


class EffectManager():
    def __init__(self, effects: list[Effect]) -> None:
        self.effects: list[Effect] = effects

    def ApplyEffects(self):
        for effect in self.effects:
            if effect.ApplyEffect():
                self.effects.remove(effect)
