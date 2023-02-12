from Base.animations import Animation, Animator
from Base.globalInfo import TupleToRandom
from Abilities.abilityEffects import EffectManager
import fightManager


class AbilityShape():
    def __init__(self, shape: list[str] = ["0X0",
                                           "XPX",
                                           "0X0"], color: str = "Red") -> None:
        self.shape: list[str] = shape
        self.color: str = color


class Ability():
    def __init__(self, speed: tuple[int, int], name: str, info: str, animation: Animation, abilityEffects: EffectManager) -> None:
        self.name: str = name
        self.info: str = info
        self.animation = animation
        self.baseSpeed: tuple[int, int] = speed
        self.speed: int = TupleToRandom(speed)
        self.abilityEffects: EffectManager = abilityEffects

    def DoAbility(self, position: tuple[int, int], animator: Animator, abilityShape: AbilityShape):
        self.doingAbility = True
        print(f"using ability at {position}")

        animator.SetAnimation(self.animation)
        # a faire afficher la zone de l'ability

        #self.entity.rect.topleft = __positionToUse

    def FinishedAbility(self):
        if not self.doingAbility:
            return
        self.doingAbility = False
        fightManager.CallNextMove()


# Melee Ability = 4 shapes, each in a different direction (up, down, left, right)
class MeleeAbility(Ability):
    def __init__(self, speed: tuple[int, int], name: str, info: str, animation: Animation, abilityEffects: EffectManager,
                 upShape: AbilityShape,
                 downShape: AbilityShape,
                 rightShape: AbilityShape,
                 leftShape: AbilityShape) -> None:
        super().__init__(speed, name, info, animation, abilityEffects)

        self.upShape: AbilityShape = upShape
        self.downShape: AbilityShape = downShape
        self.rightShape: AbilityShape = rightShape
        self.leftShape: AbilityShape = leftShape

    def GetAbilityShape(self, direction: tuple[int, int]) -> AbilityShape:
        if direction == (0, -1):
            return self.upShape
        elif direction == (0, 1):
            return self.downShape
        elif direction == (1, 0):
            return self.rightShape
        elif direction == (-1, 0):
            return self.leftShape
        else:
            print("Invalid direction for ability shape")
            return self.upShape
# Ranged Ability = 2 shapes: one for the projectile, one for the area of effect


class RangedAbility(Ability):
    def __init__(self, speed: tuple[int, int], name: str, info: str, animation: Animation, abilityEffects: EffectManager,
                 zoneShape: AbilityShape,
                 projectileShape: AbilityShape) -> None:
        super().__init__(speed, name, info, animation, abilityEffects)
