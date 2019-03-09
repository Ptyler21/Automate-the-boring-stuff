'''

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
'''

def floop(i):

    i = 0
    for number in range(10):
        print(i)
        i += 1

def wloop(i):
    i = 0
    while i < 10:
        print(i)
        i += 1


def main():
    print(floop(0))
    print(wloop(0))

if __name__=="__main__":
    main()