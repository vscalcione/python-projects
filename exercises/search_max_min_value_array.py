""" This is a simply method that use max() and min() python snippet code for searching
max and min value into an array
"""


def get_max_min_index_value(array):
    max_value = max(array)
    min_value = min(array)
    min_position = array.index(min(array))
    max_position = array.index(max(array))
    print("Max value is: ", max_value, " at position: ", max_position)
    print("Max value is: ", min_value, " at position: ", min_position)


""" This is a simply method that execute the code of max() and min() python snippet code """


def get_min_val(array):
    min_val = array[0]
    min_val_index = 0
    for i in range(0, len(array), 1):
        if min_val > array[i]:
            min_val = array[i]
            min_val_index = i
    print("Min val is ", min_val, " at position: ", min_val_index)


def get_max_val(array):
    max_val = array[0]
    max_val_index = 0
    for i in range(0, len(array), 1):
        if max_val < array[i]:
            max_val = array[i]
            max_val_index = i
    print("Max val is ", max_val, " at position: ", max_val_index)


if __name__ == "__main__":
    array = []
    length_array = int(input("Insert array length: "))
    array = []

    for i in range(length_array):
        value = int(input("Insert value: "))
        array.append(value)

    print("****** Method developed by the user **** ")
    get_max_val(array)
    get_min_val(array)

    print("\n****** Python snipped code ***** ")
    get_max_min_index_value(array)