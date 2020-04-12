from pip._vendor.distlib.compat import raw_input
import os
import time


def is_palindrome_word():
    word = raw_input("Insert word: ")
    tmp_word = ''.join(reversed(word))
    if word == tmp_word:
        print("Entered word: " + word + " is a palindrome word ")
    else:
        print("Entered word: " + word + " isn't a palindrome word ")


def print_menu():
    print("==================================================\n Palindorme Word Checker")
    print("==================================================")


if __name__ == "__main__":
    while True:
        print_menu()
        # time.sleep(2) This instruction can put on sleep mode the execution of all script
        is_palindrome_word()
        choice = raw_input("Another operation? yes/no ")
        if choice == "yes" or choice == "y":
            os.system("clear")
            is_palindrome_word()
        else:
            break
