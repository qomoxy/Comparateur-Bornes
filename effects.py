import random
import pygame


class AppliedEffect():
    def __init__(self, minDamage: int = 0, maxDamage: int = 0, minHeal: int = 0, maxHeal: int = 0) -> None:
        self.damageEffect = random.randint(minDamage, maxDamage)
        self.healEffect = random.randint(minHeal, maxHeal)


class EffectManager():
    def __init__(self, sprite: pygame.surface.Surface,
                 minTurnsToApply: int = 0, maxTurnsToApply: int = 0,
                 numberOfTimesToApply: int = 1, probabilityToApply: float = 0.5,
                 appliedEffect=AppliedEffect()) -> None:

        self.numberOfTurnsToApply: int = random.randint(
            minTurnsToApply, maxTurnsToApply)
        self.numberOfTimesToApply: int = numberOfTimesToApply
        self.probabilityToApply: float = probabilityToApply
        self.sprite: pygame.surface.Surface = sprite


offenseEffect = {
    "Bleed": EffectManager(pygame.image.load("test1.png"), 1, 4, appliedEffect=AppliedEffect(2, 5)),
    "Poisoned": EffectManager(pygame.image.load("test1.png"), 0, 5, appliedEffect=AppliedEffect(2, 3)),
    "Plage": EffectManager(pygame.image.load("test1.png"), 1, 3, appliedEffect=AppliedEffect(1, 4)),
    "Burning": EffectManager(pygame.image.load("test1.png"), 1, 3, appliedEffect=AppliedEffect(1, 3)),
    "Rot": EffectManager(pygame.image.load("test1.png"), 0, 2, appliedEffect=AppliedEffect(5, 8)),
    "Cursed": EffectManager(pygame.image.load("test1.png"), 1, 5, appliedEffect=AppliedEffect(7, 11)),
    "Doom": EffectManager(pygame.image.load("test1.png"), 1, 8, appliedEffect=AppliedEffect(2, 4))
}

defenseEffect = {
    "Heal": EffectManager(pygame.image.load("test1.png"), 1, 1, appliedEffect=AppliedEffect(minHeal=5, maxHeal=15)),
    "Recovery": EffectManager(pygame.image.load("test1.png"), 1, 5, appliedEffect=AppliedEffect(minHeal=2, maxHeal=7)),
    "Quick Heal": EffectManager(pygame.image.load("test1.png"), 1, 5, appliedEffect=AppliedEffect(minHeal=2, maxHeal=9)),

}
