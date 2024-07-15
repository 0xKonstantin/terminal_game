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
    print('Armed with a flashlight and a wooden stick you walk through the woods mid afternoon.')
    bear = classes.Character(type='Enemy Bear', name='Aggresive Bear', hp= 10)
    print('You hear a low growling sound coming from behind you, You turn around to see a wild bear.')
    print('The bear stands on its rear legs and roars at you.')
    player.in_battle = True
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
                    print(f'You swing your stick at the {bear.name} for {hit} points of damage.')
                    print(f'Your opponent has {bear.hp} remaining')
                    functions.space()
                    player.deciding = False
                    bear.turn = True
                elif(player.choice_one == '2'):
                    heal = player.heal(player,player)
                    print(f'You healed for {heal} points. Your new health is {player.hp}')
                    print(f'The {bear.name} has {bear.hp} hp remaining')
                    functions.space()
                    player.deciding = False
                    bear.turn = True
                else:
                    print('Please input a valid option.')
        else:
            print('You\'re Dead')
            player.in_battle = False
            variables.playing = False
            break
            

        # Enemy turn 
        if(bear.hp > 0):   
            if(bear.turn):       
                hit = bear.deal_damage(player)
                print(f'The bear roars and smacks you with his Paw hitting you for {hit} damage.')
                print(f'You have {player.hp} health reamining')
                bear.turn = False
                player.deciding = True
                functions.section_divde()
        else:
            player.level += 1
            functions.section_divde()
            print('The bear pushes you over and runs away, You stand up thankful to be alive.')
            print('You brush off your clothes, fix your hair and continue your hike.')
            print('Not long after you hear something rustling in the bushes.')
            player.in_battle = False
            functions.space()
        
    
    if(player.hp > 0):
        print('Two wild Racoons jump out the Bushes. They appear to be infected with rabies.')
        racoon_1 = classes.Character(type='Rabid Racoon ',name='Rabid Racoon #1',hp=10)
        racoon_2 = classes.Character(type='Rabid Racoon ',name='Rabid Racoon #2',hp=10)
        print('Foaming at the mouth and rubbing their little paws together they you hear them chatter and know they are ready to eat')
        functions.section_divde()
        player.in_battle = True
    else:
        break

    # 2nd Battle loop
    while(player.in_battle == True):
        if(player.hp > 0): 
            player.deciding = True
            # Player decision on action
            if(player.deciding == True):
                player.choice_one = input('Pick an action \n1) Attack \n2) Heal\n\nEnter 1 - 2: ')
                functions.section_divde()
                player.action_selected = True
                # Player chose attack
                while(player.action_selected == True):
                    if(player.choice_one == '1'):
                        player.target = input(f'Select your target.\n1) {racoon_1.name}\n2) {racoon_2.name} \nEnter 1-2: ')
                        functions.section_divde()
                        if(player.target == "1"):
                            if(racoon_1.hp > 0):
                                hit = player.deal_damage(racoon_1)
                                print(f'You swing your stick at the {racoon_1.name} for {hit} points of damage. Your opponent has {racoon_1.hp} remaining')
                                functions.space()
                                player.deciding = False
                                player.action_selected = False
                                racoon_1.turn = True
                                racoon_2.turn = True
                                if(racoon_1.hp <= 0):
                                    print('The Racoon scurries away to find snacky snacks')
                        elif(player.target == '2'):
                            if(racoon_2.hp > 0):
                                hit = player.deal_damage(racoon_2)
                                print(f'You swing your stick at the {racoon_2.name} for {hit} points of damage. Your opponent has {racoon_2.hp} remaining')
                                functions.space()
                                player.deciding = False
                                player.action_selected = False
                                racoon_1.turn = True
                                racoon_2.turn = True
                                if(racoon_2.hp <= 0):
                                    print('The Racoon scurries away to find snacky snacks')
                        else:
                            print('Invalid target try again.')
                            functions.space()
                        
                    elif(player.choice_one == '2'):
                        heal = player.heal(player,player)
                        print(f'You healed for {heal} points. Your new health is {player.hp}')
                        print(f'{racoon_1.name} has {racoon_1.hp} hp remaining')
                        print(f'{racoon_2.name} has {racoon_2.hp} hp remaining')
                        player.deciding = False
                        player.action_selected = False
                        racoon_1.turn = True
                        racoon_2.turn = True
                        functions.space()
                    else:
                        print('Please input a valid option')
                        player.action_selected = False
        else:
            print('You\'re Dead')
            player.in_battle = False
            variables.playing = False
            break
            

        # Enemy turn 
        if(racoon_1.hp > 0):   
            if(racoon_1.turn):       
                hit = racoon_1.deal_damage(player)
                print(f'{racoon_1.name} lunges at you biting your ankle dealing {hit} damage.')
                print(f'You have {player.hp} health reamining')
                racoon_1.turn = False
                functions.space()

        if(racoon_2.hp > 0):   
            if(racoon_2.turn):       
                hit = racoon_2.deal_damage(player)
                print(f'{racoon_2.name} scratches at your leg dealing {hit} damage.')
                print(f'You have {player.hp} health reamining')
                racoon_2.turn = False
                functions.section_divde()

        if(racoon_1.hp <= 0 and racoon_2.hp <= 0 ):
            player.in_battle = False
            print('"What is up with all these crazy Animals" You think to yourself')
            functions.space()
            

    if(player.hp > 0):
        print('You keep walking the woods till you reach a break in the trees and see a pond at the end')
        print('At the edge of the pond you see someone standing and decide to approach them.')
        print('"Odd seeing someone here, who are you?" You ask')
        functions.space()
    else:
        break
    
    mike_tyson = classes.Character(type='Boss', name='Mike Tyson', hp=100)
    print(f'{mike_tyson.name} Turns and throws an overhand right at you barely missing')
    print('Jumping back you raise your stick ready to fight')
    print('You *shouting*: "First holy Shit you\'re Mike Tyson! Second what the hell are you doing here and why you trying to kill me?"')
    functions.space()
    print('Mike: "Shut up and fight"')
    functions.section_divde()
    player.in_battle = True

    while(player.in_battle == True):
        if(player.hp > 0):
            player.deciding = True
            if(player.deciding == True):
                player.choice_one = input('Pick an action \n1) Attack \n2) Heal\n\nEnter 1 - 2: ')
                functions.section_divde()
                if(player.choice_one == '1'):
                    if(variables.round == 1):
                        hit = player.deal_damage(mike_tyson)
                        print(f'You swing your stick at {mike_tyson.name} breaking on his head for {hit} points of damage. Your opponent has {mike_tyson.hp} hp remaining')
                        print('You throw your stick on the ground and raise your fists')
                        functions.space()
                        player.deciding = False
                        mike_tyson.turn = True
                    else:
                        hit = random.randint(0,1)
                        mike_tyson.hp -= hit
                        damage = 1
                        player.hp 
                        print(f'You throw a right hook at {mike_tyson.name} hurting your hand in the process.')
                        print(f'Because you hurt your hand you take {damage} points of damage you have {player.hp} hp remaining')
                        print(f'{mike_tyson.name} takes {hit} points of damage. Your opponent has {mike_tyson.hp} hp remaining')
                        functions.space()
                        player.deciding = False
                        mike_tyson.turn = True

                elif(player.choice_one == '2'):
                    heal = player.heal(player,player)
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
            if(mike_tyson.turn and variables.round < 4):       
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
        

