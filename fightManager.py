from actions import Action
import operator


class Move():
    def __init__(self, moveToDo: Action, speed: int) -> None:
        self.moveToDo = moveToDo
        self.speed = speed


states = ["Choose Move", "Preview Moves"]
currentState = states[0]

onChoose: list[Action] = []
movesToExecute: list[Move] = []


def SortMovesBySpeed(movesToSort: list[Move]) -> list[Move]:
    return sorted(movesToSort, key=operator.attrgetter('speed'), reverse=True)


def DoMoves():
    global movesToCall, moveToCallIndex

    movesToCall = SortMovesBySpeed(movesToExecute)
    if len(movesToCall) == 0:
        return

    moveToCallIndex = 0
    CallNextMove()


def CallNextMove():
    global moveToCallIndex, currentState

    if moveToCallIndex >= len(movesToCall):
        currentState = states[0]
        moveToCallIndex = 0
        return

    moveToCallIndex += 1
    movesToCall[moveToCallIndex - 1].moveToDo.Invoke()


movesToCall: list[Move] = []
moveToCallIndex: int = 0
