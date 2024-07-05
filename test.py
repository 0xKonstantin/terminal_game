import classes, random


player = classes.Character(type='Player', name=input('What\'s your name: '), hp=10)
enemy = classes.Character(type='Enemy', name='unknown', hp=random.randint(2,10))



print(enemy.hp)