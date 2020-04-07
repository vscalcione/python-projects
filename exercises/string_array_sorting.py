from pip._vendor.distlib.compat import raw_input

if __name__ == "__main__":
    array_length = int(raw_input("Insert length of array: "))
    array = []
    for i in range(array_length):
        value = raw_input("Insert value: ")
        array.append(value)
    print(" ********* Original Array ****** ---> " + str(array))
    array.sort()
    print(" ********* Sorted Array ******* ---> " + str(array))
