from Player.playerAnimations import PlayerAnimation
from Player.playerClass import PlayerClass
from Player.playerAbilities import PlayerAbilitiesManager
from Player.playerProperties import PlayerProperties


class Player():

    def __init__(self) -> None:
        self.pClass = PlayerClass("Player", "Mage", "")
        self.pProperties = PlayerProperties()
        self.pAbilities = PlayerAbilitiesManager(self.pProperties)
        self.pAnims = PlayerAnimation()

    def Update(self, framerate: int):
        self.pAnims.UpdateAnimations(framerate)
        self.pAbilities.Update()
