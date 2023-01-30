import pygame
import events
from actions import Action
from Player.playerProperties import PlayerProperties
import grid
import globalInfo


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
    def __init__(self, pProperties: PlayerProperties) -> None:
        super().__init__(pProperties)
        events.onMousePress += [Action(self, "MoveToMouse")]

    def WhileSelected(self) -> None:
        grid.AddColoredCell(
            (self.pProperties.rect.x, self.pProperties.rect.y + globalInfo.gridSize), "Blue")
        grid.AddColoredCell(
            (self.pProperties.rect.x, self.pProperties.rect.y - globalInfo.gridSize), "Blue")
        grid.AddColoredCell(
            (self.pProperties.rect.x + globalInfo.gridSize, self.pProperties.rect.y), "Blue")
        grid.AddColoredCell(
            (self.pProperties.rect.x - globalInfo.gridSize, self.pProperties.rect.y), "Blue")

    def MoveToMouse(self):
        if not self.selected:
            return

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
        self.abilities = [MovementAbility(pProperties)]
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
