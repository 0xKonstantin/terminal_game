import math, random

class Character:
    def __init__(self, type, name, hp):
        self.type = type
        self.name = name
        self.hp = hp

        self.attack = random.randint(0,2)
        self.block = random.randint(0,3)

    def take_damage(self, damage):
        self.hp -= damage
        if(self.hp < 0):
            self.hp = 0

