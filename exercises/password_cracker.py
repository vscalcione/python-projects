import hashlib
import pyfiglet
import os


def password_cracker():
    flag = 0
    password_hash = input("Enter md5 hash: ")
    plain_passwords = {"vincenzo99", "francesco05", "mamma"}
    for element in plain_passwords:
        encoded_word = element.encode('utf-8')
        digest = hashlib.md5(encoded_word.strip()).hexdigest()
        if digest == password_hash:
            print("Password has been found")
            print("Password is: " + element)
            flag = 1
            break
    if flag == 0:
        print("password/passhphare is not in the list")


def password_cracker_by_file():
    password_hash = input("Enter md5 hash: ")
    word_list = input("File name: ")
    try:
        password_file = open(word_list, "r")
    except:
        print("No file found")
        quit()

    for word in password_file:
        encoded_word = word.encode('utf-8')
        digest = hashlib.md5(encoded_word.strip()).hexdigest()
        if digest == password_hash:
            print("Password has been found")
            print("Password is: " + word)
            flag = 1
            break
    if flag == 0:
        print("password/passhphare is not in the list")


def print_menu():
    ascii_banner = pyfiglet.figlet_format("PasswordCracker")
    print("======================================================================\n" + ascii_banner)
    print("1. Run password cracker with file encoding \n2. Run password crack with array encoding")


if __name__ == "__main__":
    while True:
        print_menu()
        choice = int(input("user ~# "))
        os.system('clear')
        if choice == 1:
            password_cracker_by_file()
            break
        elif choice == 2:
            password_cracker()
            break
        else:
            print("Error")
            break
