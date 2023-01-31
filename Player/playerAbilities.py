from time import sleep
import pygame
import events
from actions import Action
from Player.playerProperties import PlayerProperties
import grid
import globalInfo
import fightManager


class PlayerAbility():
    def __init__(self, pProperties: PlayerProperties) -> None:
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

    def __init__(self, pProperties: PlayerProperties, shapeString: list[str], color: str = "Blue") -> None:
        super().__init__(pProperties)
        self.shapeCells = grid.PositionsToCells(grid.ShapeToPositions(
            shapeString), color)
        events.onMousePress += [Action(self, "MoveToMouse")]

    def WhileSelected(self) -> None:
        grid.AddCells([grid.CellInfo((cell.position[0] + self.pProperties.rect.x,
                                      cell.position[1] + self.pProperties.rect.y),
                                     cell.color)
                      for cell in self.shapeCells])

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
        self.abilities = [MovementAbility(pProperties, ["XXXXX"
                                                        "XXXXX",
                                                        "XXPXX",
                                                        "XXXXX",
                                                        "XXXXX"])]
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
