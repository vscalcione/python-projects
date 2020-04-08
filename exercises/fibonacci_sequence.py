"""This is a recursive method that print Fibonacci Sequence"""

def fibonacci_sequence(value):
    if value == 1:
        return 1
    elif value == 2:
        return 1
    elif value > 2:
        return fibonacci_sequence(value - 1) + fibonacci_sequence(value - 2)


if __name__ == "__main__":
    print(" ***************** Fibonacci Sequence ****************** ")
    value = int(input("Insert value: "))
    print(" ======== RESULT ======== ")
    for value in range(1, value + 1):
        print(value, ":", fibonacci_sequence(value))

