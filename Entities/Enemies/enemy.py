# a refaire: inheritance avec "Entity"
from random import randint
from Base.actions import Action
import Base.animations as animations
from Entities.entity import Entity
from Abilities.abilities import Ability
import grid
from fightManager import movesToExecute, Move, CallNextMove


class Enemy():
    doingMove = False

    def __init__(self, entity: Entity, idleAnimation: animations.Animation) -> None:
        self.entity = entity

        self.currentAbility: Ability = entity.abilities[0]
        self.abilityShapePositions: list[tuple[int, int]] = []
        movesToExecute.append(Move(Action(self, "DoMove"), self.entity.speed))

        self.idleAnimation: animations.Animation = idleAnimation
        self.animator: animations.Animator = animations.Animator()
        self.animator.SetAnimation(idleAnimation)

    def DoMove(self):
        self.doingMove = True
        abilityToDo: Ability = self.entity.abilities[randint(
            0, len(self.entity.abilities) - 1)]

        __possiblePositions = grid.ShapeToPositions(
            abilityToDo.shape, self.entity.rect.topleft)
        self.abilityShapePositions = __possiblePositions

        __positionToUse = __possiblePositions[randint(
            0, len(__possiblePositions) - 1)]

        print(f"Moving {self.entity.name} to {__positionToUse}")

        self.entity.rect.topleft = __positionToUse

        self.currentAbility = abilityToDo

        self.FinishedMove()

    def FinishedMove(self):
        self.doingMove = False
        CallNextMove()

    def Update(self, framerate: int):
        self.animator.Update(framerate)
        if not self.doingMove:
            return

        grid.AddCells([grid.CellInfo(abilityShapePosition, self.currentAbility.cellColor)
                      for abilityShapePosition in self.abilityShapePositions])
