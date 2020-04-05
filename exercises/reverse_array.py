from __future__ import print_function

if __name__ == "__main__":
    array_length = int(input("Insert lenght of array: "))
    array = []
    for i in range(array_length):
        value = int(input("Insert value: "))
        array.append(value)
    
    print("********* Original array : *************")
    for i in range(0, len(array)):
        print(str(array[i]) + ",", end=" ")

    print("\n")
    print("\n********** Reverse array *********")
    for i in range(len(array) - 1, -1, -1):
        print(str(array[i]) + ",", end=" ")
    print("\n")
    

    