import math, random, classes, functions, variables


#Starts the Game
while(variables.playing):

    #Initalizes the player and requests their name
    player = classes.Character(type='Player', name=input('What\'s your name: ', hp=10))

    functions.section_divde()
    print(f'                      Welcome {player.name}')
    functions.section_divde()

    print('This Game takes place in the Woods late at night...')
    functions.space()
    print('You and some friends had gone out camping in the woods')
    print('You awaken in the middle of the night when you heard a loud scream')
    print('You hear the scream again from further away...')
    print('"That sounded like Sam" you say jumping up.')
    functions.section_divde()
    variables.choice_one = int(input('What do you do? \n\n1) Shout Sam loudly. \n2) Grab your flash light and exit your tent. \n3) Grab your phone and call Sam \n\nEnter 1-3: '))
    variables.deciding = True


    # First Choice
    while(variables.deciding):
        # Option 1 Shout Sam
        if(variables.choice_one == 1):
            functions.space()
            print('You think to yourself "I don\'t know exactly what\'s going on. I shouldn\'t make to much noise.')
            functions.section_divde()
            variables.choice_one = int(input('What do you do? \n\n1) Shout Sam loudly. \n2) Grab your flash light and go look. \n3) Grab your phone and call Sam \n\nEnter 1-3: '))


        # Option 2 Grab light and check
        elif(variables.choice_one == 2):
            functions.space()
            print('You think you yourself "I don\'t like the feeling of things.')
            print('You Grab your flash light and cell phone which reads no signal.')
            print('You put the phone in your pocket and turn on your light.')
            print('You step outside and get hit')
            variables.deciding = False
            functions.space()


        # Option 3 Grab phone n call
        elif(variables.choice_one == 3):
            functions.space()
            print('You grab your cell phone to see a no cell signal')
            functions.section_divde()
            variables.choice_one = int(input('What do you do? \n\n1) Shout Sam loudly. \n2) Grab your flash light and go look. \n3) Grab your phone and call Sam \n\nEnter 1-3: '))


        # No valid option chosen
        else:
            functions.section_divde()
            variables.choice_one = int(input('Pick a valid option. \nWhat do you do? \n\n1) Shout Sam loudly. \n2) Grab your flash light and go look. \n3) Grab your phone and call Sam \n\nEnter 1-3: '))

print('')



