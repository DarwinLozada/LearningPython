def min_number(numbers):
    counter = len(numbers)
    n = len(numbers)
    minor = numbers[n-1]
    num2 = numbers[n-2]
    counter2 = counter - 2
    while counter != 0:
        if minor >= num2:
            minor = num2
            num2 = numbers[n-counter2]
            counter2 += 1
            counter = counter - 1
        else:
            num2 = numbers[n-counter2]
            counter2 += 1
            counter = counter - 1

    print(minor)


def min_number2(numbers):
    menor = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] < menor:
            menor = numbers[i]
        i += 1
    print(menor)




listnumbers = [-122, 38423, 2, 312, 382, 8312, -22222, 11231313123214, 999, 473, -122222222]

min_number(listnumbers)
min_number2(listnumbers)
