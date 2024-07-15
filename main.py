import math, random, classes, functions, variables

variables.playing = True
#Starts the Game
while(variables.playing):

    #Initalizes the player and requests their name
    player = classes.Character(type='Player', name=input('What\'s your name: '), hp=10)
    functions.space()
    functions.space()


    print(f'Welcome to The Matrix {player.name}')
    functions.section_divde()
    print('Armed with a wooden sword and a wooden sheild you\'re walking through the woods')
    bear = classes.Character(type='Enemy Bear', name='Aggresive Bear', hp= 10)
    print('You\'re walking through the woods when a wild bear jumps out at you.')
    player.in_battle = True
    print('The bear stands on its rear legs roaring.')
    player.deciding = True
    functions.section_divde()


    # 1st Battle loop with one enemy
    while(player.in_battle == True):
        if(player.hp > 0):
            if(player.deciding == True):
                player.choice_one = input('Pick an action \n1) Attack \n2) Heal\n\nEnter 1 - 2: ')
                functions.section_divde()
                if(player.choice_one == '1'):
                    hit = player.deal_damage(bear)
                    print(f'You swing your sword at the {bear.name} for {hit} points of damage. Your opponent has {bear.hp} remaining')
                    functions.space()
                    player.deciding = False
                    bear.turn = True
                elif(player.choice_one == '2'):
                    heal = player.heal(player)
                    print(f'You healed for {heal} points. Your new health is {player.hp}')
                    player.deciding = False
                    bear.turn = True
                    functions.space()
                else:
                    input('Please input a valid option: ')
        else:
            print('You\'re Dead')
            player.in_battle = False
            variables.playing = False
            break
            

        # Enemy turn 
        if(bear.hp > 0):   
            if(bear.turn):       
                hit = bear.deal_damage(player)
                print(f'The bear roars and slashes you with his Paw hitting you for {hit} damage.')
                print(f'You have {player.hp} health reamining')
                bear.turn = False
                player.deciding = True
                functions.section_divde()
        else:
            print('You killed the bear, barely escpaing with your life.')
            player.in_battle = False
            functions.section_divde()
        
    
    if(player.hp <= 0):
        break

    print('Thankful for your now broken sword you survive and continue your hike.')
    print('You hear something rustling in the bushes.')
    racoon_1 = classes.Character(type='Rabid Racoon ',name='Rabid Racoon 1',hp=10)
    racoon_2 = classes.Character(type='Rabid Racoon ',name='Rabid Racoon 2',hp=10)
    print('Two wild Racoons jump out the Bushes. They appear to be rabid infected.')
    player.in_battle = True

    # 2nd Battle loop
    while(player.in_battle == True):
        if(player.hp > 0): 
            player.deciding = True
            # Player decision on action
            if(player.deciding == True):
                player.choice_one = input('Pick an action \n1) Attack \n2) Heal\n\nEnter 1 - 2: ')
                functions.section_divde()
                # Player chose attack
                if(player.choice_one == '1'):
                    player.target = input(f'Select your target.\n1) {racoon_1.name}\n2) {racoon_2.name} \nEnter 1-2: ')
                    if(player.target == "1"):
                        if(racoon_1.hp > 0):
                            hit = player.deal_damage(racoon_1)
                            print(f'You swing your sword at the {racoon_1.type} for {hit} points of damage. Your opponent has {racoon_1.hp} remaining')
                            functions.space()
                            player.deciding = False
                            racoon_1.turn = True
                            racoon_2.turn = True
                            if(racoon_1.hp <= 0):
                                print('The Racoon scurries away to find snacky snacks')
                        else:
                            print('Invalid target try again.')
                    elif(player.target == '2'):
                        if(racoon_2.hp > 0):
                            hit = player.deal_damage(racoon_2)
                            print(f'You swing your sword at the {racoon_2.type} for {hit} points of damage. Your opponent has {racoon_2.hp} remaining')
                            functions.space()
                            player.deciding = False
                            racoon_1.turn = True
                            racoon_2.turn = True
                            if(racoon_2.hp <= 0):
                                print('The Racoon scurries away to find snacky snacks')
                        else:
                            print('Invalid target try again.')
                elif(player.choice_one == '2'):
                    heal = player.heal(player)
                    print(f'You healed for {heal} points. Your new health is {player.hp}')
                    player.deciding = False
                    racoon_1.turn = True
                    racoon_2.turn = True
                    functions.space()
                else:
                    input('Please input a valid option: ')
        else:
            print('You\'re Dead')
            player.in_battle = False
            variables.playing = False
            break
            

        # Enemy turn 
        if(racoon_1.hp > 0):   
            if(racoon_1.turn):       
                hit = racoon_1.deal_damage(player)
                print(f'The {racoon_2.name} roars and slashes you with his Paw hitting you for {hit} damage.')
                print(f'You have {player.hp} health reamining')
                racoon_1.turn = False
                functions.section_divde()

        if(racoon_2.hp > 0):   
            if(racoon_2.turn):       
                hit = racoon_2.deal_damage(player)
                print(f'The {racoon_2.name} roars and slashes you with his Paw hitting you for {hit} damage.')
                print(f'You have {player.hp} health reamining')
                racoon_2.turn = False
                functions.section_divde()

        if(racoon_1.hp <= 0 and racoon_2.hp <= 0 ):
            print('"What is up with all these crazy Animals" You think to yourself')
            player.in_battle = False

    if(player.hp <= 0):
        break
      
    print('You keep walking the woods till you reach a pond at the end')
    print('At the edge of the pond you see someone standing and decide to approach them.')
    print('"Odd seeing someone here, who are you?" You ask')
    mike_tyson = classes.Character(type='Boss', name='Mike Tyson', hp=100)
    print(f'{mike_tyson.name} Turns and throws a right hand at you barely missing')
    print('You jump back and prepare to fight')
    player.in_battle = True
    while(player.in_battle == True):
        if(player.hp > 0):
            player.deciding = True
            if(player.deciding == True):
                player.choice_one = input('Pick an action \n1) Attack \n2) Heal\n\nEnter 1 - 2: ')
                functions.section_divde()
                if(player.choice_one == '1'):
                    hit = player.deal_damage(mike_tyson)
                    print(f'You throw a right hand at {mike_tyson.name} for {hit} points of damage. Your opponent has {mike_tyson.hp} hp remaining')
                    functions.space()
                    player.deciding = False
                    mike_tyson.turn = True
                elif(player.choice_one == '2'):
                    heal = player.heal(player)
                    print(f'You healed for {heal} points. Your new health is {player.hp}')
                    player.deciding = False
                    mike_tyson.turn = True
                    functions.space()
                else:
                    input('Please input a valid option: ')
        else:
            print('You awake in your bed to see it was all a weird ass dream.')
            player.in_battle = False
            variables.playing = False
            break
            

        # Enemy turn 
        if(mike_tyson.hp > 0):
            if(mike_tyson.turn and variables.round < 3):       
                hit = mike_tyson.deal_damage(player)
                print(f'{mike_tyson.name} throws a jab at you hitting you for {hit} damage.')
                print(f'You have {player.hp} health reamining')
                mike_tyson.turn = False
                variables.round += 1
                functions.section_divde()
            else:
                hit = 100000
                player.hp -= hit
                print(f'Mike Tyson throws an overhand right connecting on your jaw dealing {hit} damage')
                print(f'You have {player.hp} health reamining')
        

