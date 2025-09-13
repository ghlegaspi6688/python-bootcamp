from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health=10, defense=10):
        self.health = health
        self.defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

class Knight(Character):
    def __init__(self, health=10, defense=10):
        super().__init__(health, defense)
        #self.attack = attack

    def attack(self, other):
        #damage = self.strength - other.
        damage = self.defense - other.defense
        other.health -= damage
        print(other.health)

class Mage(Character):
    def __init__(self, health, defense, magic):
        super().__init__(health, defense)
        self.magic = magic

    def attack(self, other):
        damage = self.magic - other.defense
        other.health -= damage
        print(other.health)

class Warrior(Character):
    def __init__(self, health, defense, strength):
        super().__init__(health, defense)
        self.strength = strength

    def attack(self, other):
        damage = self.strength - other.defense
        other.health -= damage
        print(other.health)

knight = Knight()
knight.attack(knight)
