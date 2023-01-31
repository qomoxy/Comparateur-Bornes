from time import sleep
import pygame
from abilities import Ability
from effects import EffectManager
from entity import Entity
import events
from actions import Action
import grid
import fightManager


class PlayerAbility(Ability):
    def __init__(self, pEntity: Entity, speed: tuple[int, int], name: str, info: str, abilityEffects: EffectManager, cellColor: str = "Red", shape: list[str] = ...) -> None:
        super().__init__(speed, name, info, abilityEffects, cellColor, shape)
        self.pEntity = pEntity

    selected = False

    def Select(self) -> None:
        self.selected = True
        return

    def WhileSelected(self) -> None:
        return

    def Deselect(self) -> None:
        self.selected = False
        return


class PlayerAbilitiesManager():
    selectedAbility = None
    abilities: list[PlayerAbility] = []

    def __init__(self, pEntity: Entity) -> None:
        self.pEntity = pEntity
        # [MovementAbility(pEntity, speed=(5, 8), name="Move", info="Move to new position", abilityEffects=EffectManager([]), cellColor="Blue", shape=["••X••",
        self.abilities = []
        #                                                                                                                                         "•XXX•",
        #                                                                                                                                         "XXPXX",
        #                                                                                                                                         "•XXX•",
        #                                                                                                                                         "••X••"])]
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
