import pygame
import Abilities.abilities as abilities
from Abilities.abilityEffects import EffectManager
from Entities.entity import Entity
import Base.events as events
from Base.actions import Action
import grid
from fightManager import DoMoves


class PlayerAbility(abilities.Ability):
    def __init__(self, baseAbility: abilities.Ability) -> None:
        super().__init__(baseAbility.baseSpeed, baseAbility.name,
                         baseAbility.info, baseAbility.abilityEffects,
                         baseAbility.cellColor, baseAbility.shape)

    selected = False

    def Select(self) -> None:
        self.selected = True
        return

    def WhileSelected(self) -> None:
        return

    def Deselect(self) -> None:
        self.selected = False
        return


class PlayerMovementAbility(PlayerAbility):
    def __init__(self, baseAbility: abilities.Ability, entity: Entity) -> None:
        super().__init__(baseAbility)
        self.baseAbility = baseAbility
        self.shapeCellPositions = grid.ShapeToPositions(baseAbility.shape)
        self.entity = entity
        events.onMousePress += [Action(self, "TryMoveToPosition")]

    def TryMoveToPosition(self):
        if not self.selected:
            return

        targetPos: tuple[int, int] = grid.ClampToGrid(pygame.mouse.get_pos())

        for cellPosition in self.shapeCellPositions:
            if (cellPosition[0] + self.entity.rect.x, cellPosition[1] + self.entity.rect.y) == targetPos:
                break
        else:
            return

        print("Moving")

        DoMoves()

        self.entity.rect = pygame.Rect(
            targetPos[0], targetPos[1], self.entity.rect.width, self.entity.rect.height)

    def WhileSelected(self) -> None:
        super().WhileSelected()
        grid.AddCells([grid.CellInfo((cellPosition[0] + self.entity.rect.x,
                                      cellPosition[1] + self.entity.rect.y),
                                     self.cellColor)
                       for cellPosition in self.shapeCellPositions])


class PlayerAbilitiesManager():
    selectedAbility = None

    def __init__(self, pEntity: Entity) -> None:
        self.pEntity = pEntity
        movementAbility = PlayerMovementAbility(abilities.Ability((3, 6), name="Move", info="Move the player", abilityEffects=EffectManager([]), cellColor="Blue", shape=["••X••",
                                                                                                                                                                          "•XXX•",
                                                                                                                                                                          "XXPXX",
                                                                                                                                                                          "•XXX•",
                                                                                                                                                                          "••X••"]),
                                                pEntity)
        self.abilities: list[PlayerAbility] = [movementAbility]
        self.SelectAbility(0)

    def SelectAbility(self, abilityIndex: int):
        if self.selectedAbility != None:
            self.selectedAbility.Deselect()

        if abilityIndex == -1:
            self.selectedAbility = None
        else:
            self.selectedAbility = self.abilities[abilityIndex]
            self.selectedAbility.Select()

    def Update(self):
        if self.selectedAbility != None:
            self.selectedAbility.WhileSelected()
