import pygame as pygame
from Base.actions import Action

playerInput: list = [0, 0]

onMousePress: list[Action] = []


def HandleEvents() -> None:

    global playerInput
    playerInput = UpdateMoveInput()

    for event in pygame.event.get():
        CheckKeys(event)
        CheckQuit(event)


def CheckQuit(event: pygame.event.Event) -> None:
    if event.type != pygame.QUIT:
        return
    pygame.quit()
    exit()


def CheckKeys(event: pygame.event.Event) -> None:
    if event.type == pygame.MOUSEBUTTONDOWN:
        for action in onMousePress:
            action.Invoke()


def UpdateMoveInput() -> list[int]:
    newInput: list = [0, 0]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        newInput[0] -= 1
    if keys[pygame.K_RIGHT]:
        newInput[0] += 1
    if keys[pygame.K_UP]:
        newInput[1] -= 1
    if keys[pygame.K_DOWN]:
        newInput[1] += 1

    return newInput
