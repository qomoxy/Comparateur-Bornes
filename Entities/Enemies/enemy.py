from random import randint

import pygame
from Abilities.abilityEffects import EffectManager, Effect
from Base.actions import Action
from Base.animations import Animation, Animator
from Entities.entity import Entity
from Abilities.abilities import Ability
import grid
from fightManager import movesToExecute, Move, CallNextMove


class EnemyProperties():
    def __init__(self, entity: Entity, idleAnimation: Animation) -> None:
        self.entity = entity
        self.idleAnimation = idleAnimation


__slimeIdleAnim = Animation(
    spriteSheet=pygame.image.load("Sprites/slime.png"),
    loop=True, length=.6,
    sheetSpriteCount=(12, 1), spriteAnchor=(0, .5),
    startEndFrames=(0, 1))

__slimeJumpAnim = Animation(
    spriteSheet=pygame.image.load("Sprites/slime.png"),
    loop=False, length=1.2,
    sheetSpriteCount=(12, 1), spriteAnchor=(0, .5),
    startEndFrames=(2, 11))

enemies = {
    "Slime": EnemyProperties(
        entity=Entity(3, "Slime", "Un slime", (0, 0),
                      [Ability((5, 10), "Saut", "Boing !", __slimeJumpAnim,
                               EffectManager([Effect(damage=(2, 4))]), shape=["•X•",
                                                                              "XPX",
                                                                              "•X•"])]),
        idleAnimation=__slimeIdleAnim)
}


class Enemy():
    doingMove = False

    def __init__(self, properties: EnemyProperties, startPosition: tuple[int, int]) -> None:
        self.entity = properties.entity
        self.entity.rect.topleft = startPosition

        for ability in properties.entity.abilities:
            ability.animation.onAnimationFinishAction = Action(
                self, "FinishedMove")

        self.currentAbility: Ability = properties.entity.abilities[0]
        self.abilityShapePositions: list[tuple[int, int]] = []
        movesToExecute.append(Move(Action(self, "DoMove"), self.entity.speed))

        self.idleAnimation: Animation = properties.idleAnimation
        self.animator: Animator = Animator()
        self.animator.SetAnimation(properties.idleAnimation)

    def DoMove(self):
        self.doingMove = True
        abilityToDo: Ability = self.entity.abilities[randint(
            0, len(self.entity.abilities) - 1)]

        __possibleAbilityPositions = grid.ShapeToPositions(
            abilityToDo.shape, self.entity.rect.topleft)
        self.abilityShapePositions = __possibleAbilityPositions

        __positionToUse = __possibleAbilityPositions[randint(
            0, len(__possibleAbilityPositions) - 1)]

        print(f"{self.entity.name} using ability at {__positionToUse}")

        self.animator.SetAnimation(abilityToDo.animation)

        #self.entity.rect.topleft = __positionToUse

        self.currentAbility = abilityToDo

    def FinishedMove(self):
        if not self.doingMove:
            return
        self.doingMove = False
        CallNextMove()

    def Update(self, framerate: int):
        self.animator.Update(framerate)
        if not self.doingMove:
            return

        grid.AddCells([grid.CellInfo(abilityShapePosition, self.currentAbility.cellColor)
                      for abilityShapePosition in self.abilityShapePositions])
