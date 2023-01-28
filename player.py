import pygame
import events


class Player():
    currentMoveCooldown: float = 0
    moveCooldown: float = .3
    rect = pygame.Rect(0, 0, 10, 10)

    def Update(self, framerate: int):

        self.currentMoveCooldown -= 1/framerate

        if self.currentMoveCooldown > 0:
            return

        if events.playerInput == [0, 0]:
            return

        self.rect.x += events.playerInput[0]
        self.rect.y += events.playerInput[1]

        self.currentMoveCooldown = self.moveCooldown

        print(
            f"Le joueur va dans la direction: {events.playerInput} et est maintenant a [{self.rect.x} {self.rect.y}]")

    def Blit(self, screen: pygame.surface.Surface):
        screen.blit(pygame.Surface(
            # *50 est temporaire
            [50, 50]), (self.rect.x * 50, self.rect.y * 50))
