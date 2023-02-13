from Entities.Player.playerAnimations import PlayerAnimation
from Entities.Player.playerAbilitiesManager import PlayerAbilitiesManager
from Abilities.abilityEffects import EffectManager
from Entities.entity import Entity


class PlayerProperties():
    def __init__(self, pEntity: Entity, pAbilitiesManager: PlayerAbilitiesManager) -> None:
        self.pEntity = pEntity
        self.pAbilitiesManager = pAbilitiesManager


class Player():

    def __init__(self, pProperties:  PlayerProperties) -> None:
        self.pProperties = pProperties
        self.pEntity = pProperties.pEntity
        self.pAbilitiesManager = pProperties.pAbilitiesManager
        self.pAnims = PlayerAnimation()

    def Update(self, framerate: int):
        self.pAnims.UpdateAnimations(framerate)
        self.pAbilitiesManager.Update()
