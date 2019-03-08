#The Following program will have a user guess a random number

import random
import sys
randmNumber = random.randint(1,21)
print("Hello Welcome to the random number program!")

try:
    while True:
        userInput = int(input("Please give me a random number between 1 and 20"))

        if userInput < 0:
            print("Nice try...")
        print(randmNumber)
        if userInput < randmNumber:
            print("good guess!")
        elif userInput > randmNumber:
            print("too far!")
        elif userInput == randmNumber:
            print("congrats")
            break
except ValueError:
    print(" Error: You put in the wrong thing try again")
except KeyboardInterrupt:
    print("\nHow dare you!")

