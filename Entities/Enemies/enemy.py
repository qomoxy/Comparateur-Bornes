# a refaire: inheritance avec "Entity"
from random import randint
from Base.actions import Action
from Entities.entity import Entity
from Abilities.abilities import Ability
import grid
from fightManager import movesToExecute, Move


class Enemy():
    doingMove = False

    def __init__(self, entity: Entity) -> None:
        self.entity = entity
        self.currentAbility: Ability = entity.abilities[0]
        self.abilityShapePositions: list[tuple[int, int]] = []
        movesToExecute.append(Move(Action(self, "DoMove"), self.entity.speed))

    def DoMove(self):
        abilityToDo: Ability = self.entity.abilities[randint(
            0, len(self.entity.abilities) - 1)]

        __possiblePositions = grid.ShapeToPositions(
            abilityToDo.shape, (self.entity.rect.x, self.entity.rect.y))
        self.abilityShapePositions = __possiblePositions

        __positionToUse = __possiblePositions[randint(
            0, len(__possiblePositions) - 1)]

        print(__positionToUse)

        self.doingMove = True
        self.currentAbility = abilityToDo

    def Update(self):
        if not self.doingMove:
            return

        grid.AddCells([grid.CellInfo(abilityShapePosition, self.currentAbility.cellColor)
                      for abilityShapePosition in self.abilityShapePositions])
