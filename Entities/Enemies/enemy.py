# a refaire: inheritance avec "Entity"
class Enemy:

    def __init__(self, name: str, classe: str, type: str, description: str, health: int, damage: int, defense: int, speed: int, loot: str) -> None:
        self.name = name
        self.classe = classe
        self.type = type
        self.description = description
        self.effectList: list = []
        self.health = health
        self.damage = damage
        self.defense = defense
        self.speed = speed
        self.loot = loot

    def __str__(self) -> str:
        return f"{self.name} voici vos compétences: \n health : {self.health} \n damage : {self.damage} \n defense : {self.defense} \n speed : {self.speed}"
