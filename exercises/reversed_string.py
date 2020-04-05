from pip._vendor.distlib.compat import raw_input


def reverse_string():
    inserted_string = raw_input("Insert value: ")
    print("************* Original string -> " + inserted_string + " ************** ")
    str = ""
    for index in inserted_string:
        str = index + str
    print("************* Reversed string: -> " + str + " ************** ")


if __name__ == "__main__":
    while True:
        print("Phrase Reverser ")
        reverse_string()
        response = raw_input("Do you reverse another string? y/s: ")
        if response == "yes" or response == "y":
            reverse_string()
        else:
            break
