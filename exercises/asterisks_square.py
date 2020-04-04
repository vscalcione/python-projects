from __future__ import print_function

def print_square(value):
    print()
    i = 0
    while (i < value):
        j = 0
        while (j < value):
            j = j + 1
            print('*', end = '  ')
        i = i + 1
        print('')

if __name__ == '__main__':
    while True:
        value = int(input("Insert value: "))
        if value > 0:
            print_square(value)
            break
        else:
            print()
            print("You insert a negative value")