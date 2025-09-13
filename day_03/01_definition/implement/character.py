class Character:
    def __init__(self, health=10, strength=10, defense=10):
        self.health = health
        self.strength = strength
        self.defense = defense
    def attack(self, other):     #self attack enemy
        damage = self.strength - other.defense # 100 - 10 = 90
        other.health -= damage # 10 (enemy strength) - 90 = -80

player = Character(strength=100)
enemy = Character()
player.attack(enemy)
print(enemy.health)
