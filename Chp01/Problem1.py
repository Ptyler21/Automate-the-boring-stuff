'''
9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
'''


def block01(spam):
    spam = 1
    if spam == 1:
        return("Hello")
def block02(spam):
    spam = 2
    if spam == 2:
        return("Howdy!")
def block03(spam):
    spam = 3
    if spam == 3:
        return("greetings!")
def main():


    print(block01(3))
    print(block02(2))
    print(block03(3))

if __name__=="__main__":
    main()