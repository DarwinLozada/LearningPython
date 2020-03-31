def maxandmin(numbers):
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    print("this is the max number {}".format(max_number))

    index = 1
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:

            min_number = numbers[index]
            index += 1
    print("this is the min number {}".format(min_number))


def main():
    inputnumbers = None
    list_numbers = []

    while inputnumbers != "End":
        inputnumbers = input("Tell me a number ")
        if inputnumbers != "End":
            number = int(inputnumbers)
            list_numbers.append(number)

    maxandmin(list_numbers)


if __name__ == "__main__":
    main()
