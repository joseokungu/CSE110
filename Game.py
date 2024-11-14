'''
Author : Jose Okitandende 
'''

print('Hello, welcome to your adventure game')

answer = input('You are at a crossroad, would you like to go LEFT, RIGHT or FORWARD?')
if answer.upper() == 'LEFT':
    answer = input('You encounter a monster, would like to RUN or ATTACK? ')
    if answer.upper() == 'ATTACK':
        answer = input('The monster is armed, do you need a KNIFE or GUN')
        if answer.upper() == 'KNIFE':
            print('That was not the best idea, Sorry you lost?')
        elif answer.upper() == 'GUN':
            print('Aha! brillant idea, You have killed the monster. You won!')
        else:
            print('Please exit!')
    elif answer.upper() == 'RUN':
        answer = input('Why choose run? Are you not brave enough? Do you wish to CONTINUE or ABORT mission?')
        if answer.upper() == 'CONTINUER':
            answer = input('Nice one! I commend your bravery. Do you want to choose an ARROW or a DANGER?')
            if answer.upper() == 'ARROW':
                print('Good choice, you have killed the monster, You lost!')
            else:
                print('Your option is invalid')
        elif answer.upper() == 'ABORT':
            print('Poor coward! You lost the game!')
        else:
            print('No other options left! Please exit!')
    else:
        print('Invalid option, please exit!')

elif answer.upper() == 'RIGHT':
    answer = input('There is a goul-like creature, do you wish to FIGHT or FLEE?')
    if answer.upper() == 'FIGHT':
        print('You are so brave! You have killed the goul with the knife you found by your side. congrats!')
    elif answer.upper() == 'FLEE':
        answer = input('Why so scared? it is just a game! Do you still want to PLAY or EXIT?')
        if answer.upper() == 'PLAY':
            print('Nice choice, You have a gun! kill the goul!')
            print('Congrats! You have killed it!')
        elif answer.upper() == 'EXIT':
            print('Sorry coward! try again next time') 
        else:
            print('Please try again later, Thanks!')
    else:
        print('Please, enter a valid option') 

elif answer.upper() == 'FORWARD':
    answer = input('This option is boring, do you wish to PROCEED or QUIT?')
    if answer.upper() == 'PROCEED':
        print('It is a lonely path, you are alaone in this journey! Mission failed! try other options')
    elif answer.upper() =='QUIT':
        answer = input('Okay, have a lovely day!')
    else:
        print('Please leave the game now!')

else:
    print('That is too bad, Game over!')