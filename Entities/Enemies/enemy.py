from random import randint

import pygame
from Abilities.abilities import Ability
from Abilities.abilityEffects import EffectManager, Effect
from Base.animations import Animation, Animator
from Entities.entity import Entity

import grid


class EnemyProperties():
    def __init__(self, entity: Entity, idleAnimation: Animation) -> None:
        self.entity = entity
        self.idleAnimation = idleAnimation


class Enemy():
    doingAbility = False

    def ChooseAbility(self):
        return self.abilities[randint(
            0, len(self.abilities) - 1)]

    def __init__(self, properties: EnemyProperties) -> None:
        self.properties = properties
        self.entity = properties.entity
        self.abilities = properties.entity.abilities
        self.idleAnimation: Animation = properties.idleAnimation
        self.animator: Animator = Animator()
        self.animator.SetAnimation(properties.idleAnimation)

        # a appeller par fightManager
        self.ChooseAbility()

    def Update(self, framerate: int):
        self.animator.Update(framerate)
        if not self.doingAbility:
            return

        # grid.AddCells([grid.CellInfo(abilityShapePosition, self.currentAbility.cellColor)
            #   for abilityShapePosition in self.abilityShapePositions])
