from time import sleep


def adding(number, number2):
    result = number + number2
    return result


def subtract(number, number2):
    result = number - number2
    return result


def multiply(number, number2):
    result = number * number2
    return result


def divide(number, number2):
    result = number / number2
    return result


def only_choose_operation(first_operator, second_operator):
    operation_selected = str(input("Which operation do you wanna use? (add/subtract/multiply/divide) "))
    if operation_selected == "add":
        result = adding(first_operator, second_operator)
        print(result)

    elif operation_selected == "subtract":
        result = subtract(first_operator, second_operator)
        print(result)

    elif operation_selected == "multiply":
        result = multiply(first_operator, second_operator)
        print(result)

    elif operation_selected == "divide":
        result = divide(first_operator, second_operator)
        print(result)


def keep_operating_ask(resultentry):
    keep_loop = True

    while keep_loop:
        keep_loop2 = True
        loop_question = input("Do you want to keep operating? (Yes/No) ")
        if loop_question == "Yes":
            if keep_loop2:
                i = keep_operating_result(resultentry)
                if not i:
                    choose_operation_and_operate()
                elif i:
                    pass

        elif loop_question == "No":
            print("Good bye")
            return 0


def keep_operating_result(result):
    keep_result = input("Do you want to keep operating the last result? (Yes/No) ")
    if keep_result == "Yes":
        other_operator = int(input("Give the other number to operate "))
        only_choose_operation(result, other_operator)
        return True
    elif keep_result == "No":
        return False


def choose_operation_and_operate():
    first_operator = int(input("Give me the first number "))
    result = 0
    second_operator = int(input("Give me the second number "))
    operation_selected = str(input("Which operation do you wanna use? (add/subtract/multiply/divide) "))
    if operation_selected == "add":
        result = adding(first_operator, second_operator)
    elif operation_selected == "subtract":
        result = subtract(first_operator, second_operator)
    elif operation_selected == "multiply":
        result = multiply(first_operator, second_operator)
    elif operation_selected == "divide":
        result = divide(first_operator, second_operator)
    print(result)
    return result


def clear_result():
    pass


def main():
    keep_loop = True
    print("Welcome user")
    sleep(2)
    while keep_loop:
        result = choose_operation_and_operate()
        a = keep_operating_ask(result)
        if a == 0:
            break


if __name__ == "__main__":
    main()
