def FindIntersection(strArr):
    matches = []
    for number in strArr[0]:
        if number.isdigit():
            if number not in matches:
                for number2 in strArr[1]:
                    if number2.isdigit() and number2 == number:
                        matches.append(number)
    # code goes here
    return matches


# keep this function call here
print(FindIntersection(input("")))
