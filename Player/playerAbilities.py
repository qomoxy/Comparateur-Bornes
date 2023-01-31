from time import sleep
import pygame
from Abilities import Ability
from effects import EffectManager
import events
from actions import Action
from Player.playerProperties import PlayerProperties
import grid
import fightManager


class PlayerAbility(Ability):
    def __init__(self, pProperties: PlayerProperties, speed: tuple[int, int], name: str, info: str, abilityEffects: EffectManager, cellColor: str = "Red", shape: list[str] = ...) -> None:
        super().__init__(speed, name, info, abilityEffects, cellColor, shape)
        self.pProperties = pProperties

    selected = False

    def Select(self) -> None:
        self.selected = True
        return

    def WhileSelected(self) -> None:
        return

    def Deselect(self) -> None:
        self.selected = False
        return


class MovementAbility(PlayerAbility):

    def __init__(self, pProperties: PlayerProperties, speed: tuple[int, int], name: str, info: str, abilityEffects: EffectManager, cellColor: str = "Red", shape: list[str] = ...) -> None:
        super().__init__(pProperties, speed, name, info, abilityEffects, cellColor, shape)
        events.onMousePress += [Action(self, "MoveToMouse")]
        self.shapeCellPositions = grid.ShapeToPositions(shape)

    def WhileSelected(self) -> None:
        grid.AddCells([grid.CellInfo((cellPosition[0] + self.pProperties.rect.x,
                                      cellPosition[1] + self.pProperties.rect.y),
                                     self.cellColor)
                      for cellPosition in self.shapeCellPositions])

    def MoveToMouse(self):
        if not self.selected:
            return

        fightManager.DoMoves()

        mousePos: tuple[int, int] = pygame.mouse.get_pos()

        targetPos: tuple[int, int] = grid.ClampToGrid(mousePos)

        print(targetPos)

        self.pProperties.rect = pygame.Rect(
            targetPos[0], targetPos[1], self.pProperties.rect.width, self.pProperties.rect.height)


class PlayerAbilitiesManager():
    selectedAbility = None
    abilities: list[PlayerAbility] = []

    def __init__(self, pProperties: PlayerProperties) -> None:
        self.pProperties = pProperties
        self.abilities = [MovementAbility(pProperties, speed=(5, 8), name="Move", info="Move to new position", abilityEffects=EffectManager([]), cellColor="Blue", shape=["••X••",
                                                                                                                                                                          "•XXX•",
                                                                                                                                                                          "XXPXX",
                                                                                                                                                                          "•XXX•",
                                                                                                                                                                          "••X••"])]
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
