import sqlite3
import string
import sys
import itertools
import operator
import os
from functools import partial
from datetime import date

from Xlib.support import connect

MONTHS = "ABCDEHLMPRST"
DISPAIR = [1, 0, 5, 7, 9, 13, 15, 17, 19, 21, 2, 4, 18, 20, 11, 3, 6, 8, 12, 14, 16, 10, 22, 25, 24, 23]
ORD_0 = ord("0")
ORD_A = ord("A")
previuos_vocal = partial(operator.contains, set("AEIOUÀÈÉÌÒÙ"))


def pair(char):
    return ord(char) - (ORD_0 if char.isdigit() else ORD_A)


def dispair(char):
    return DISPAIR[ord(char) - (ORD_0 if char.isdigit() else ORD_A)]


def calculate_last_char(rest):
    return chr(ORD_A + rest)


def partition(pred, iterable):
    partitions = [], []
    for element in iterable:
        partitions[int(pred(element))].append(element)
    return partitions


def encoding_name(name, is_surname=True):
    name = name.upper().replace(" ", "")
    consonants, vocals = partition(previuos_vocal, name)
    if not is_surname and len(consonants) > 3:
        del consonants[1]
    name = "".join(consonants + vocals)[:3]
    return name.ljust(3, "X")


def encode_date(date, sex):
    offset = 40 if sex in "fF" else 0
    return "{:>02}{}{:>02}".format(date.year % 100, MONTHS[date.month - 1], date.day + offset)


def encode_comune(comune_name):
    try:
        comune_name = comune_name.upper()
        connection = sqlite3.connect("comuni.db")
        result_set = connection.execute("select code from comuni where name = ?", [comune_name])
        result = result_set.fetchone()
        return result[0]
    except TypeError:
        raise ValueError("Comune not found!! ")


def calculate_control_code(code):
    control_pair = sum(dispair(x) for x in code[::2])
    control_dispair = sum(pair(x) for x in code [1::2])
    return calculate_last_char((control_pair + control_dispair) % 26)


def calculate_cf(surname, name, date, sex, comune_name):
    code = "{}{}{}{}".format(encoding_name(surname),
                             encoding_name(name, is_surname=False),
                             encode_date(date, sex),
                             encode_comune(comune_name))
    return "".join([code, calculate_control_code(code)])


def parse_input():
    if 1 < len(sys.argv) < 6:
        exit("Number of params not sufficient")
    elif len(sys.argv) == 1:
        name = input("Name: ")
        surname = input("Surname: ")
        sex = input("Sex (M/F): ")
        birth_date = input("Date (gg/mm/aa): ")
        comune_name = input("Comune name: ")
    else:
        name, surname, sex, birth_date, comune_name = sys.argv[1:]

    if sex not in "mMfF" or len(sex) != 1:
        exit("Sex not valid! ")

    try:
        day, month, year = map(int, birth_date.split("/"))
        birth_date = date(year, month, day)
    except ValueError:
        exit("Date not valid! ")

    return surname, name, birth_date, sex, comune_name


if __name__ == "__main__":
    while True:
        print("========= Fiscal Code Calculator ============")
        data = parse_input()
        message = "Car{} {} {}, your fiscal code is:  "
        print(message.format("a" if data[3] in "fF" else "o",
                             data[1].capitalize(),
                             data[0].capitalize())
              )
        print(calculate_cf(*data))
        choice = input("Another operation? y/n ")
        if choice == "no":
            break