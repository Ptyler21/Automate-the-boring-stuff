#The Following program will have a user guess a random number

import random

print("Hello Welcome to the random number program!")

try:

    userInput = int(input("Please give me a random number between 1 and 20"))
    '''
    
    if userInput < 0:
        print("Nice try...") 
        try: 
            userInput = int(input("Please give me a POSITIVE number between 1 and 20: " ))
        except
    '''
except ValueError or KeyboardInterrupt:
    print(" Error: You put in the wrong thing try again")
