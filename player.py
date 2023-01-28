import events as events


class Player():
    position = [0, 0]
    currentMoveCooldown: float = 0
    moveCooldown: float = .3

    def Update(self, framerate: int):

        self.currentMoveCooldown -= 1/framerate

        if self.currentMoveCooldown > 0:
            return

        if events.playerInput == [0, 0]:
            return

        self.position = [self.position[0] + events.playerInput[0],
                         self.position[1] + events.playerInput[1]]
        self.currentMoveCooldown = self.moveCooldown

        print(
            f"Le joueur va dans la direction: {str(events.playerInput)} et est maintenant a {str(self.position)}")
