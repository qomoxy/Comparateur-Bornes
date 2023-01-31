class Action():
    def __init__(self, source: object, functionToCallName: str) -> None:
        self.obj = source
        self.functionToCallName = functionToCallName

    def Invoke(self):
        return getattr(self.obj, self.functionToCallName)()
