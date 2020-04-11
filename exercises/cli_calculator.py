import platform
from os import system

import sys
from os import system

import math

from pip._vendor.distlib.compat import raw_input


# Method that acquire input 2 values and adds them up ##
def sum():
    num1 = raw_input("Insert first value: ");
    num2 = raw_input("Insert second value: ")
    result = float(num1) + float(num2);
    print("Sum to: " + num1 + " and " + num2 + " : " + str(result))


# Method that acquire input 2 values and subs them up ##
def difference():
    num1 = raw_input("Insert first value: ")
    num2 = raw_input("Insert second value: ")
    if num1 > num2:
        result = float(num1) - float(num2)
    else:
        result = float(num2) - float(num1)
    print("Difference to: " + num1 + " and " + num2 + " : " + str(result))


# Method that acquire input 2 values and multiply them up ##
def multiply():
    num1 = raw_input("Insert first value: ")
    num2 = raw_input("Insert second value: ")
    result = float(num1) * float(num2)
    print("Product to: " + num1 + " and " + num2 + " : " + str(result))


# Method that acquire input 2 values and divede them up ##
def quotient():
    num1 = raw_input("Insert first value: ")
    num2 = raw_input("Insert second value: ")
    if num1 > num2 and num1 != 0:
        result = float(num1) / float(num2)
    else:
        print("Error")
    print("Quotient to : " + num1 + " and " + num2 + " : " + str(result))


# Method that acquire input 1 value and calculate the factorial of this value ##
def factorial():
    num = raw_input("Insert value: ")
    result = math.factorial(num)
    print("Factorial of: " + num + " : " + str(result))


# Method that acquire input 2 values (base, exponent) and calculate the pow ##
def pow():
    base = raw_input("Insert base: ")
    exponent = raw_input("Insert exponent: ")
    result = math.pow(float(base), float(exponent))
    print("Pow of " + base + " elevate to: " + exponent + " : " + str(result))


# Method that acquire a value and calculate its square ##
def number_square():
    num = raw_input("Insert value: ")
    result = float(num) ** 2
    print("Square of " + num + " : " + str(result))


# Method that acquire a value and calculate its cube ##
def number_cube():
    num = raw_input("Insert value: ")
    result = float(num) ** 3
    print("Square of " + num + " : " + str(result))


# Method that cleans the screen with a command that changes according to the operating system in use ##
def clear_screen_by_os():
    os = platform.system()
    if os == "Linux":
        system("clear")
    if os == "Windows":
        system("cls")


# Method that print the menu ##
def print_menu():
    print('\n'
          ' ===================================================================\n'
          '|      _____        _____      _            _       _               |\n'
          '|     |  __ \      / ____|    | |          | |     | |              |\n'
          '|     | |__) |   _| |     __ _| | ___ _   _| | __ _| |_ ___  _ __   |\n'
          '|     |  ___/ | | | |    / _` | |/ __| | | | |/ _` | __/ _ \| \'__|  |\n'
          '|     | |   | |_| | |____ (_| | | (__| |_| | | (_| | |_ (_) | |     |\n'
          '|     |_|    \__, |\_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|     |\n'
          '|             __/ |                                                 |\n'
          '|            |___/                                                  |\n'
          '|                                                                   |\n'
          '|     Developed by:  Scalcione Vincenzo                             |                  \n'
          ' ===================================================================\n'
          '    ')

    print(''' 
        1. --> Sum
        2. --> Difference
        3. --> Product
        4. --> Quotient
        5. --> Factorial
        6. --> Pow
        7. --> Square of a number
        8. --> Cube of a number
        9. --> Quit
    ''')


recursive_choice = "y";
while recursive_choice == "y":
    py_calc_prompt = "user ~# "
    print_menu()
    choice = raw_input(py_calc_prompt);
    clear_screen_by_os()
    if choice == "1":
        sum()
    elif choice == "2":
        difference()
    elif choice == "3":
        multiply()
    elif choice == "4":
        quotient()
    elif choice == "5":
        factorial()
    elif choice == "6":
        pow()
    elif choice == "7":
        number_square()
    elif choice == "8":
        number_cube()
    elif choice == "9":
        sys.exit
        break
    recursive_choice = raw_input("{ --- Do you execute another operation y/n --- } " + py_calc_prompt);
    clear_screen_by_os()
    if recursive_choice != "y":
        break
