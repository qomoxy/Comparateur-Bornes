from Player.playerAnimations import PlayerAnimation
from Player.playerClass import PlayerClass
from Player.playerMovement import PlayerMovement


class Player():
    def __init__(self, pClass: PlayerClass, pMovement: PlayerMovement, pAnims: PlayerAnimation) -> None:
        self.pClass = pClass
        self.pMovement = pMovement
        self.pAnims = pAnims

    def Update(self, framerate: int):
        self.pMovement.UpdateMovement(framerate)
        self.pAnims.UpdateAnimations(framerate)
