from globalInfo import TupleToRandom
from effects import EffectManager


class Ability():
    def __init__(self, speed: tuple[int, int], name: str, info: str, abilityEffects: EffectManager, cellColor: str = "Red", shape: list[str] = ["•••",
                                                                                                                                                "•P•",
                                                                                                                                                "•••"]) -> None:
        self.name: str = name
        self.info: str = info
        self.speed: int = TupleToRandom(speed)
        self.shape = shape
        self.cellColor = cellColor
        self.abilityEffects: EffectManager = abilityEffects


"""
class MovementAbility(Ability):

    def __init__(self, pEntity: Entity, speed: tuple[int, int], name: str, info: str, abilityEffects: EffectManager, cellColor: str = "Red", shape: list[str] = ...) -> None:
        super().__init__(pEntity, speed, name, info, abilityEffects, cellColor, shape)
        events.onMousePress += [Action(self, "MoveToMouse")]
        self.shapeCellPositions = grid.ShapeToPositions(shape)

    def WhileSelected(self) -> None:
        grid.AddCells([grid.CellInfo((cellPosition[0] + self.pEntity.rect.x,
                                      cellPosition[1] + self.pEntity.rect.y),
                                     self.cellColor)
                      for cellPosition in self.shapeCellPositions])

    def MoveToMouse(self):
        if not self.selected:
            return

        fightManager.DoMoves()

        mousePos: tuple[int, int] = pygame.mouse.get_pos()

        targetPos: tuple[int, int] = grid.ClampToGrid(mousePos)

        for cellPosition in self.shapeCellPositions:
            if (cellPosition[0] + self.pEntity.rect.x, cellPosition[1] + self.pEntity.rect.y) == targetPos:
                break
        else:
            return

        print(targetPos)

        self.pEntity.rect = pygame.Rect(
            targetPos[0], targetPos[1], self.pEntity.rect.width, self.pEntity.rect.height)"""
