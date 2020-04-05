from pip._vendor.distlib.compat import raw_input


def print_line_1():
    print('Row 1\nRow 2')
    name = raw_input("What's your name? ")
    print("Hello " + name)
    print("Hello " * 3)
    value = '''This is a multi-line string'''
    print(value)


def print_line_2(value):
    print(value[0:3])
    print(value[:3])
    print(value[3:3])
    print(value[3:4])
    print(value[5:8])
    print(value[-3: -1])
    print(value[-3:])


def print_menu():
    print("1. String pt.1 ")
    print("2. String pt. 2")


if __name__ == "__main__":
    while True:
        print_menu()
        choice = int(input("Insert your choice: "))
        if choice < 1 or choice > 2:
            print("Error")
        else:
            if choice == 1:
                print_line_1()
                break
            if choice == 2:
                statement = raw_input("Insert statement here: ")
                print_line_2(statement)
                break
