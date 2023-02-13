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


# Contient les propriétés d'une ability (dégats, soin, vitesse)
class AbilityProperties():
    def __init__(self, speed: tuple[int, int], damage: tuple[int, int], healing: tuple[int, int]) -> None:
        self.speed: tuple[int, int] = speed
        self.damage: tuple[int, int] = damage
        self.healing: tuple[int, int] = healing

    def GetSpeed(self) -> int:
        return TupleToRandom(self.speed)

    def GetHealing(self) -> int:
        return TupleToRandom(self.healing)

    def GetDamage(self) -> int:
        return TupleToRandom(self.damage)

# Contient les infos d'une ability (nom, description, animation)


class AbilityInfo():
    def __init__(self, name: str, info: str, animation: Animation) -> None:
        self.name: str = name
        self.info: str = info
        self.animation = animation


class Ability():
    def __init__(self, abilityProperties: AbilityProperties, abilityInfo: AbilityInfo, abilityEffects: EffectManager) -> None:
        self.abilityInfo = abilityInfo
        self.abilityProperties: AbilityProperties = abilityProperties
        self.abilityEffects: EffectManager = abilityEffects

    def DoAbility(self, position: tuple[int, int], animator: Animator, abilityShape: AbilityShape):
        self.doingAbility = True
        print(f"using ability at {position}")

        animator.SetAnimation(self.abilityInfo.animation)

    def WhileDoingAbility(self, position: tuple[int, int], abilityShape: AbilityShape):
        self.abilityShapePositions = grid.GetShapePositions(
            position, abilityShape.shape)

    def FinishedAbility(self):
        if not self.doingAbility:
            return
        self.doingAbility = False
        fightManager.CallNextMove()


# Melee Ability = 4 shapes, each in a different direction (up, down, left, right)
class MeleeAbility(Ability):
    def __init__(self, abilityProperties: AbilityProperties, abilityInfo: AbilityInfo, abilityEffects: EffectManager,
                 upShape: AbilityShape,
                 downShape: AbilityShape,
                 rightShape: AbilityShape,
                 leftShape: AbilityShape) -> None:
        super().__init__(abilityProperties, abilityInfo, abilityEffects)

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
    def __init__(self, abilityProperties: AbilityProperties, abilityInfo: AbilityInfo, abilityEffects: EffectManager,
                 zoneShape: AbilityShape,
                 projectileShape: AbilityShape) -> None:
        super().__init__(abilityProperties, abilityInfo, abilityEffects)
        self.zoneShape: AbilityShape = zoneShape
        self.projectileShape: AbilityShape = projectileShape
