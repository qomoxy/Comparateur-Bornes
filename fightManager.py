from Base.actions import Action
import operator
import grid


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
    global __movesToCall, __moveToCallIndex, currentState

    __movesToCall = SortMovesBySpeed(movesToExecute)
    if len(__movesToCall) == 0:
        return
    __moveToCallIndex = 0
    currentState = states[1]
    CallNextMove()


def CallNextMove():
    global __moveToCallIndex, currentState

    if __moveToCallIndex >= len(__movesToCall):
        currentState = states[0]
        __moveToCallIndex = 0
        return

    __moveToCallIndex += 1
    __movesToCall[__moveToCallIndex - 1].moveToDo.Invoke()


__movesToCall: list[Move] = []
__moveToCallIndex: int = 0
