from Entities.Player.playerAnimations import PlayerAnimation
from Entities.Player.playerClass import PlayerClass
from Entities.Player.playerAbilitiesManager import PlayerAbilitiesManager
from Abilities.abilities import Ability
from Abilities.abilityEffects import EffectManager
from Entities.entity import Entity


class Player():

    def __init__(self) -> None:
        self.pClass = PlayerClass("Player", "Mage", "")
        self.pEntity = Entity(15, (256, 256), name="Player", info="The player",
                              baseSpeed=(3, 6), baseDefense=(3, 6), effectsToApply=EffectManager([]))
        self.pAbilitiesManager = PlayerAbilitiesManager(self.pEntity)
        self.pAnims = PlayerAnimation()

    def Update(self, framerate: int):
        self.pAnims.UpdateAnimations(framerate)
        self.pAbilitiesManager.Update()
