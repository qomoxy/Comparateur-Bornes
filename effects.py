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
    "Bleed": EffectManager(pygame.image.load("test1.png"), minTurnsToApply=1, maxTurnsToApply=3, appliedEffect=AppliedEffect(minDamage=1, maxDamage=3)),
    "Poisoned": EffectManager(pygame.image.load("test1.png"), minTurnsToApply=0, maxTurnsToApply=5, appliedEffect=AppliedEffect(minDamage=1, maxDamage=2)),
    "Plague": EffectManager(pygame.image.load("test1.png"), minTurnsToApply=0, maxTurnsToApply=5, appliedEffect=AppliedEffect(minDamage=2, maxDamage=4)),
    "Burning": EffectManager(pygame.image.load("test1.png"), minTurnsToApply=1, maxTurnsToApply=2, appliedEffect=AppliedEffect(minDamage=3, maxDamage=3)),
    "Cursed": EffectManager(pygame.image.load("test1.png"), minTurnsToApply=8, maxTurnsToApply=12, appliedEffect=AppliedEffect(minDamage=2, maxDamage=4))
}

defenseEffect = {
    "Heal": EffectManager(pygame.image.load("test1.png"), minTurnsToApply=1, maxTurnsToApply=1, appliedEffect=AppliedEffect(minHeal=5, maxHeal=5)),
    "Recovery": EffectManager(pygame.image.load("test1.png"), minTurnsToApply=3, maxTurnsToApply=5, appliedEffect=AppliedEffect(minHeal=2, maxHeal=2)),
    "Quick Heal": EffectManager(pygame.image.load("test1.png"), minTurnsToApply=2, maxTurnsToApply=3, appliedEffect=AppliedEffect(minHeal=1, maxHeal=3)),

}
