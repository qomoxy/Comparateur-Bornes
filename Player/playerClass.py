import random


class PlayerClass:

    def __init__(self, name: str, classe: str, info: str):
        self.name = name
        self.classe = classe
        self.info = info
        self.effectList: list = []

    def type_classes(self, classe):
        if classe == "Mage":
            self.health = 15
            self.damage = random.randint(8, 20)
            self.defense = random.randint(0, 5)
            self.speed = random.randint(2, 5)

        elif classe == "Swordman":
            self.health = 20
            self.damage = random.randint(5, 15)
            self.defense = random.randint(3, 10)
            self.speed = random.randint(5, 10)

        elif classe == "Assasin":
            self.health = 15
            self.damage = random.randint(8, 19)
            self.defense = random.randint(0, 5)
            self.speed = random.randint(5, 15)

        else:  # classe == "Tank"
            self.health = 40
            self.damage = random.randint(3, 7)
            self.defense = random.randint(10, 25)
            self.speed = random.randint(0, 4)

    def __str__(self) -> str:  # test
        return f"{self.name} voici vos compétences: \n health : {self.health} \n damage : {self.damage} \n defense : {self.defense} \n speed : {self.speed}"
