import classes, random


player = classes.Character(type='player', name='K', hp=10)
enemy = classes.Character(type='Enemy', name='unknown', hp=10)



while(enemy.hp > 0):
    player.deal_damage(enemy)

    print(enemy.hp)