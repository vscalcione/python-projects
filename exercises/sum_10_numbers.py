def sum_values(limit):
    sum = 0
    for i in range(1, limit + 1):
        value = int(input("Insert value " + str(i) + " : "))
        sum += value
    print("Sum is: " + str(sum))


if __name__ == "__main__":
    limit = int(input("Limit? "))
    sum_values(limit)

