import math, random

class Character:
    def __init__(self, type, name, hp):
        self.name = name
        self.hp = hp
        self.level = 1

        if(type == "player"):
            self.type = 'Player'
            self.in_battle = False
            self.deciding = False
            self.target = 0
            self.in_battle = False
            self.playing = True
            self.choice_one = 0
            self.choice_two = 0
            self.choice_three = 0
            self.action_selected = True
            self.armed = True
            

        else:
            self.type = 'Enemy'
            self.action = random.randint(1,3)
            self.turn = False

    def deal_damage(self, target):  
        damage = random.randint(0,3)
        target.hp -= damage
         
        if target.hp < 0:
            target.hp = 0  
        return damage

    def heal(self, caster, target):
        healed = caster.level * random.randint(2,4)
        target.hp += healed
        if(target.hp < 0):
            target.hp = 0
        return healed
        



