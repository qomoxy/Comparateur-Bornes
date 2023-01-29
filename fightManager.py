from actions import Action
import fightManager

onAttackChoose: list[Action] = [Action(fightManager, "Test")]

states = ["Choose Attack", "AttackPreview"]
currentState = states[0]


def Test():
    print("TEST")
