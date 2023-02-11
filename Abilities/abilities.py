from Base.animations import Animation, Animator
from Base.globalInfo import TupleToRandom
from Abilities.abilityEffects import EffectManager
import fightManager


class Ability():
    def __init__(self, speed: tuple[int, int], name: str, info: str, animation: Animation, abilityEffects: EffectManager, cellColor: str = "Red", shape: list[str] = ["•••",
                                                                                                                                                                      "•P•",
                                                                                                                                                                      "•••"]) -> None:
        self.name: str = name
        self.info: str = info
        self.animation = animation
        self.baseSpeed: tuple[int, int] = speed
        self.speed: int = TupleToRandom(speed)
        self.shape = shape
        self.cellColor = cellColor
        self.abilityEffects: EffectManager = abilityEffects

    def DoAbility(self, position: tuple[int, int], animator: Animator, direction: tuple[int, int] = (0, 1)):
        self.doingAbility = True
        # abilityToDo: Ability = self.entity.abilities[randint(
        #    0, len(self.entity.abilities) - 1)]

        # __possibleAbilityPositions = grid.ShapeToPositions(
        #    abilityToDo.shape, self.entity.rect.topleft)
        #self.abilityShapePositions = __possibleAbilityPositions

        # __positionToUse = __possibleAbilityPositions[randint(
        #    0, len(__possibleAbilityPositions) - 1)]

        print(f"using ability at {position}")

        animator.SetAnimation(self.animation)

        #self.entity.rect.topleft = __positionToUse

    def FinishedAbility(self):
        if not self.doingAbility:
            return
        self.doingAbility = False
        fightManager.CallNextMove()
