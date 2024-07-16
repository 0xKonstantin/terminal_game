import math, random, classes, functions, variables

variables.playing = True
#Starts the Game
while(variables.playing):

    #Initalizes the player and requests their name
    player = classes.Character(type='Player', name=input('Enter your name: '), hp=10)
    functions.space()
    functions.space()


    print(f'Welcome to The Matrix {player.name}')
    functions.section_divde()
    print('Armed with a flashlight and a wooden stick you decide to take a hike through the woods mid afternoon.')
    player.armed = True
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
                    print(f'Your opponent has {bear.hp} health remaining.')
                    functions.space()
                    player.deciding = False
                    bear.turn = True
                elif(player.choice_one == '2'):
                    heal = player.heal(player,player)
                    print(f'You healed for {heal} points. You have {player.hp} health remaining.')
                    print(f'The {bear.name} has {bear.hp} health remaining.')
                    functions.space()
                    player.deciding = False
                    bear.turn = True
                else:
                    print('Please input a valid option.')
        else:
            print('You\'re Dead.')
            player.in_battle = False
            variables.playing = False
            break
            

        # Enemy turn 
        if(bear.hp > 0):   
            if(bear.turn):       
                hit = bear.deal_damage(player)
                print(f'The bear roars and smacks you with his Paw hitting you for {hit} damage.')
                print(f'You have {player.hp} health remaining.')
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
        print('Foaming at the mouth and rubbing their little paws together you can hear them chatter.')
        print('You can tell they are hungry ready to eat. You search your pocket for some snacky snacks.')
        print('Unable to find anything your only option is to fight. You raise your stick and preapare for battle.')
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
                                print(f'You swing your stick at the {racoon_1.name} for {hit} points of damage.')
                                print(f'Your opponent has {racoon_1.hp} health remaining.')
                                functions.space()
                                player.deciding = False
                                player.action_selected = False
                                racoon_1.turn = True
                                racoon_2.turn = True
                                if(racoon_1.hp <= 0):
                                    print('The Racoon scurries away to find snacky snacks.')
                        elif(player.target == '2'):
                            if(racoon_2.hp > 0):
                                hit = player.deal_damage(racoon_2)
                                print(f'You swing your stick at the {racoon_2.name} for {hit} points of damage.')
                                print(f'Your opponent has {racoon_2.hp} health remaining.')
                                functions.space()
                                player.deciding = False
                                player.action_selected = False
                                racoon_1.turn = True
                                racoon_2.turn = True
                                if(racoon_2.hp <= 0):
                                    print('The Racoon scurries away to find snacky snacks.')
                        else:
                            print('Invalid target try again.')
                            functions.space()
                        
                    elif(player.choice_one == '2'):
                        heal = player.heal(player,player)
                        print(f'You healed for {heal} points. You have {player.hp} health remaining.')
                        print(f'{racoon_1.name} has {racoon_1.hp} health remaining.')
                        print(f'{racoon_2.name} has {racoon_2.hp} health remaining.')
                        player.deciding = False
                        player.action_selected = False
                        racoon_1.turn = True
                        racoon_2.turn = True
                        functions.space()
                    else:
                        print('Please input a valid option.')
                        player.action_selected = False
        else:
            print('You\'re Dead.')
            player.in_battle = False
            variables.playing = False
            break
            

        # Enemy turn 
        if(racoon_1.hp > 0):   
            if(racoon_1.turn):       
                hit = racoon_1.deal_damage(player)
                print(f'{racoon_1.name} lunges at you biting your ankle dealing {hit} damage.')
                print(f'You have {player.hp} health remaining.')
                racoon_1.turn = False
                functions.space()

        if(racoon_2.hp > 0):   
            if(racoon_2.turn):       
                hit = racoon_2.deal_damage(player)
                print(f'{racoon_2.name} scratches at your leg dealing {hit} damage.')
                print(f'You have {player.hp} health remaining.')
                racoon_2.turn = False
                functions.section_divde()

        if(racoon_1.hp <= 0 and racoon_2.hp <= 0 ):
            player.in_battle = False
            print('"What is up with all these crazy Animals" You think to yourself.')
            functions.space()
            

    if(player.hp > 0):
        print('You keep walking the woods till you reach a break in the trees and see a pond.')
        mike_tyson = classes.Character(type='Boss', name='Mike Tyson', hp=100)
        print('At the edge of the pond you see someone standing and decide to approach them.')
        print(f'You: "Odd seeing someone here this late, I\'m {player.name} who are you?"')
        functions.space()
    else:
        break
    
    print(f'The Unknown person turns and throws an overhand right at you barely missing.')
    print(f'Jumping back you raise your stick ready to fight. You look closer and realize it\'s {mike_tyson.name}.')
    functions.space()
    print('You: "First and foremost you\'re Mike Tyson! Second what the heck are you doing here and why you trying to kill me?"')
    print('Mike: "Shut up and fight."')
    functions.section_divde()
    player.in_battle = True

    while(player.in_battle == True):
        if(player.hp > 0):
            player.deciding = True
            if(player.deciding == True):
                player.choice_one = input('Pick an action \n1) Attack \n2) Heal\n\nEnter 1 - 2: ')
                functions.section_divde()
                if(player.choice_one == '1'):
                    if(player.armed == True):
                        hit = player.deal_damage(mike_tyson)
                        print(f'You swing your stick at {mike_tyson.name} breaking it on his head for {hit} points of damage.')
                        print(f'Your opponent has {mike_tyson.hp} health remaining.')
                        print('You throw your stick on the ground and raise your fists.')
                        player.deciding = False
                        player.armed = False
                        mike_tyson.turn = True
                        functions.space()
                    else:
                        hit = random.randint(0,1)
                        mike_tyson.hp -= hit
                        damage = 1
                        player.hp 
                        print(f'You throw a right hook at {mike_tyson.name} hurting your hand in the process.')
                        print(f'Hurting yourself in the process you take {damage} points of damage, you have {player.hp} health remaining.')
                        print(f'{mike_tyson.name} takes {hit} points of damage. Your opponent has {mike_tyson.hp} health remaining.')
                        functions.space()
                        player.deciding = False
                        mike_tyson.turn = True

                elif(player.choice_one == '2'):
                    heal = player.heal(player,player)
                    print(f'You healed for {heal} points. You have {player.hp} health remaining.')
                    print(f'{mike_tyson.name} has {mike_tyson.hp} health remaining.')
                    player.deciding = False
                    mike_tyson.turn = True
                    functions.space()
                else:
                    print('Please input a valid option.')
        else:
            print('You awake in your bed to see it was all a weird ass dream.')
            player.in_battle = False
            variables.playing = False
            functions.space()
            break
            

        # Enemy turn 
        if(mike_tyson.hp > 0):
            if(mike_tyson.turn and variables.round < 4):       
                hit = mike_tyson.deal_damage(player)
                print(f'{mike_tyson.name} throws a jab at you hitting you for {hit} damage.')
                print(f'You have {player.hp} health remaining.')
                mike_tyson.turn = False
                variables.round += 1
                functions.section_divde()
            elif(mike_tyson.turn and variables.round == 4):
                hit = 100000
                player.hp -= hit
                if(player.hp < 0):
                    player.hp = 0
                print(f'Mike Tyson throws an overhand right connecting on your jaw dealing {hit} damage.')
                print(f'You have {player.hp} health remaining.')
        

