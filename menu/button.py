import pygame


class Button():
    def __init__(self, x, y,  image: pygame.surface.Surface, scale) -> None:
        self.width = image.get_width()
        self.height = image.get_height()
        self.coordonnees = (x, y)
        self.image = pygame.transform.scale(
            image, (int(self.width * scale), int(self.height * scale)))
        self.rect: pygame.rect.Rect = self.image.get_rect()
        self.clicked = False

        def draw(self, surface):
            clic = False
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            surface.blit(self.image, (self.rect.x, self.rect.y))

        # return action
