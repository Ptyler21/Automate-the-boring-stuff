import sys
'''
parameter example
name = 'david'
print(name)

Enter number:
3
10
5
16
8
4
2
1
'''
try:

    number = int(input("Please input a number: "))
except ValueError:
    print("You must input an integer")
def collatz(number):

        if number % 2 == 0:
            number = number // 2
            #print("This is even printing",number)
            return number
        elif number % 2 == 1:
            number = 3 * number + 1
            #print("This is odd printing",number)
            return number
while collatz(number) != 1:
    number = collatz(number)
    print(number)

print(collatz(number))