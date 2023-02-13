from Abilities.abilities import Ability
from Entities.Enemies.enemy import Enemy
from Entities.Player.player import Player
import grid

__turnOrder: list[Ability] = []
__turnIndex: int = 0


def PlayerChoosingAbility():
    print("Player is choosing ability")


def DoTurns(playerAbility: Ability, playerAbilitySpeed: int, enemyAbilities: list[Ability], enemySpeeds: list[int]):
    global __turnOrder, __turnIndex

    __allAbilities = [playerAbility] + enemyAbilities
    __allSpeeds = [playerAbilitySpeed] + enemySpeeds
    __allAbilitiesAndSpeeds = dict(zip(__allAbilities, __allSpeeds))

    __turnOrder = SortTurnOrder(__allAbilitiesAndSpeeds)
    __turnIndex = 0

# create a class that contains the ability to do and the speed of the entity that will do it


def SortTurnOrder(__unsortedAbilitiesAndSpeeds: dict[Ability, int]) -> list[Ability]:
    # sort the abilities by speed
    __sortedAbilitiesAndSpeeds = sorted(
        __unsortedAbilitiesAndSpeeds.items(), key=lambda item: item[1])
    # return the abilities in the order they will be used
    return [ability for ability, _ in __sortedAbilitiesAndSpeeds]


def TurnFinished():
    global __turnIndex
    if __turnIndex >= len(__turnOrder):
        return
