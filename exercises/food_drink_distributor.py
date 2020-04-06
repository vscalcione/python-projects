from pip._vendor.distlib.compat import raw_input
from operator import eq
import os


def brew_drink_or_food(amount, price):
    while amount < price:
        if amount < price:
            tmp = 0
            tmp = float(tmp + amount)
            print("Amount too low. Insert other coins")
            amount = float(raw_input("Insert coins: "))
            amount = tmp + amount
        else:
            if amount == price:
                print("Rest not payable")
                break
    rest = float(amount - price)
    print("Product dispensed, Your rest is: " + str(round(rest, 3)))


def print_menu():
    print("\n **************** Food & Drink Distributor **************** ")
    print("1. Coffe \n2. Thea \n3. Orange juice \n4. Sandwich1 \n5. Sandwich2")
    print("************************************************************")

if __name__ == "__main__":
    while True:
        os.system("clear")
        print_menu()
        product_code = int(raw_input("Code product: "))
        if product_code < 1 or product_code > 5:
            print("Error. Not allowed choice. ")
            product_code = int(raw_input("Code product: "))
        if product_code == 1:
            coins = float(raw_input("Insert coin: "))
            brew_drink_or_food(coins, 0.80)
        elif product_code == 2:
            coins = float(raw_input("Insert coin: "))
            brew_drink_or_food(coins, 1.10)
        elif product_code == 3:
            coins = float(raw_input("Insert coin: "))
            brew_drink_or_food(coins, 1.20)   
        elif product_code == 4:
            coins = float(raw_input("Insert coin: "))
            brew_drink_or_food(coins, 1.40)  
        elif product_code == 5:
            coins = float(raw_input("Insert coin: "))
            brew_drink_or_food(coins, 1.60)
        choice = raw_input("Another selection? y/n ")
        if not (eq(choice, "y") or eq(choice, "yes")):
            break  
