def contains_0():
    zeros = 0
    while True:
        value = input("Insert value: ")
        if int(value) < 0:
            break
        else:
            if int(value) == 0:
                zeros = zeros + 1
    return zeros


def contains_at_least_0():
    contains_at_least_0 = False
    while True:
        value = input("Insert value: ")
        if int(value) < 0:
            break
        else:
            if int(value) == 0:
                contains_at_least_0 = True
    return contains_at_least_0


def print_menu():
    print("\n************************ Menu ******************************")
    print("1. Counts if there is at least one 0 in a sequence of values")
    print("2. Counts how many 0s are present in a sequence of values\n")
    print("************************ End Menu ******************************")


if __name__ == "__main__":
    print_menu()
    choice = int(input("Your choice is: "))
    if choice == 1:
        result = contains_at_least_0()
        if result:
            print("The sequence of values taken as input contains at least one 0")
        else:
            print("The sequence of values taken as input not contains 0s ")
    else:
        result = contains_0()
        print("In this sequence there are " + str(result) + " zeros ")
