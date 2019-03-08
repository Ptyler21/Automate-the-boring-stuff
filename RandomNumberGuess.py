#The Following program will have a user guess a random number

import random
import sys
randNumber = random.randint(1,21)
print("Hello Welcome to the random number program!")


i = 0
try:
    while i < 7:
        userInput = int(input("Please give me a random number between 1 and 20: "))

        if userInput < 0:
            print("Nice try...")
            sys.exit(0)
        if userInput < randNumber:
            print("good guess!")
        elif userInput > randNumber:
            print("too far!")
        elif userInput == randNumber:
            print("congrats")
            break
        #print(randmNumber)
        i = i + 1
        print("You have {} attempts left!".format(7 - i))
        userAttempts = 7 - i
        if userAttempts == 0:
            print("Aww the number I was looking for was {}".format(randNumber))
except ValueError:
    print(" Error: You put in the wrong thing try again")
except KeyboardInterrupt:
    print("\nHow dare you!")

