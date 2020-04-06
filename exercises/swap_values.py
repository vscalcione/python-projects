from pip._vendor.distlib.compat import raw_input


def swap_variables():
    first_value = raw_input("Insert first value: ")
    second_value = raw_input("Insert second value: ")
    tmp_var = first_value
    first_value = second_value
    second_value = tmp_var
    print("First value: " + first_value)
    print("Second value: " + second_value)


if __name__ == "__main__":
    swap_variables()
