from Player.playerAnimations import PlayerAnimation
from Player.playerClass import PlayerClass
from Player.playerAbilities import PlayerAbilitiesManager
from abilities import Ability
from effects import EffectManager
from entity import Entity


class Player():

    def __init__(self) -> None:
        self.pClass = PlayerClass("Player", "Mage", "")
        self.pEntity = Entity(15, name="Player", info="The player",
                              baseSpeed=(3, 6), baseDefense=(3, 6), effectsToApply=EffectManager([]))
        self.pAbilities = PlayerAbilitiesManager(self.pEntity)
        self.pAnims = PlayerAnimation()

    def Update(self, framerate: int):
        self.pAnims.UpdateAnimations(framerate)
        self.pAbilities.Update()
