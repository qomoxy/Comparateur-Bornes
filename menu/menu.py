import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def mainMenu():
    screen = pygame.display.set_mode((64*16, 64*9))
    BackGround = Background('background_image.png', [0, 0])

    screen.fill([255, 255, 255])
    # screen.blit(BackGround.image, BackGround.rect)

    run = True
    while run:
        mousePose = pygame.mouse.get_pos()
