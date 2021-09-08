"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

def start_game():
    print('''  
==============================================  

  /\ /V\    
|~||~||~|  
| || || |  QUICK! THERE HAS BEEN A BOMB FOUND!
|(~)T(~)|   
=/1  10\=  THE ONLY WAY TO DEFUSE IT IS WITH A
|| _.  ||  NUMBER 1 - 10! START NOW!
| \/  / |
|_/^^^\_|

==============================================
''')
    high_score = 0
    while True:
        if high_score == False:
            print('THERE IS NO HIGH SCORE YET.\n')
        else:
            print(f'HIGH SCORE: {high_score}\n')
        random_number = random.randint(1, 10)
        tries = 1
        print('ENTER A NUMBER 1 - 10 TO BEGIN. ')        
        while True:
            try:
                guess = int(input(">  "))
                if guess < 1 or guess > 10:
                    print('THAT NUMBER IS OUTSIDE OF THE RANGE.\nPLEASE ENTER ONLY NUMBERS 1 - 10.\n')
                    continue
                if guess < random_number:
                    print('IT\'S HIGHER. TRY AGAIN.\n')
                    tries += 1
                    continue
                if guess > random_number:
                    print('IT\'S LOWER. TRY AGAIN.\n')
                    tries += 1
                    continue
                if guess == random_number:
                    print(f'YOU\'RE A HERO!\nIT TOOK YOU {tries} TRIES TO GUESS {random_number}.\nYOU SUCCESSFULLY DEFUSED THE BOMB.\n')
                    break
            except ValueError:
                print('SORRY! YOU ENTERED AN INCORRECT VALUE. TRY AGAIN WITH A NUMBER 1 - 10 ')
                tries += 1
                continue
                
        if high_score == 0 or tries < high_score:
            high_score = tries
        replay = input('WOULD YOU LIKE TO PLAY AGAIN?\nENTER Y TO PLAY AGAIN.  >> ')
        if replay.lower() == 'y':
            continue
        else:
            print('UNTIL NEXT TIME THEN... ')
            break                
            
start_game()
