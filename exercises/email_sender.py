import smtplib
from getpass import getpass
import os


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    sender_email = input(str("Insert email: "))
    password = getpass("Insert password: ")
    if server.login(sender_email, password):
        print("Login success")
        receiver_email = input(str("Insert email to send: "))
        message = input(str("Message: "))
        server.sendmail(sender_email, receiver_email, message)
        print("Email has been sendend by: " + sender_email)
    else:
        print("Login error")


def print_menu():
    print("==================================================\n Email Sender")
    print("==================================================")


if __name__ == "__main__":
    while True:
        print_menu()
        send_email()
        choice = input(str("Another operation? yes/no "))
        if choice == "yes" or choice == "y":
            os.system("clear")
            send_email()
        else:
            break
