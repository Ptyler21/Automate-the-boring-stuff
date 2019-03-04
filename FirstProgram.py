# This program says hello and asks for my name

'''
Expected output:

Hello!
What's your name?: Phillip
It is nice to meet you Phillip
The length of your name is: 7
What is your age: 22
You will be 23 in a year!
'''

print("Hello!")

userName = input("What's your name?: ")

#Print out their name in a sentence
ProgGreeting = print("It is nice to meet you {}".format(userName))

#print the length of their name
nameLen = len(userName)
print("The lenth of your name is: {}".format(nameLen))

#ask the user for their age
userAge = int(input("What is your age?: "))

#Print out their age next year in a sentence
ageStatement = print("You will be {} in a year! ".format(userAge + 1))
