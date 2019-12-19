import random
from time import sleep

REST_TIME = 3


def main():
    pharses_list = []
    user_phrase = ""

    while not user_phrase == "End":
        user_phrase = input("Submit a phrase: ")
        if not user_phrase == "End":
            pharses_list.append(user_phrase)

    if pharses_list:
        phrase = random.choice(pharses_list)
        while pharses_list:
            for phrase in pharses_list:
                print(phrase)
                sleep(REST_TIME)
                pharses_list.remove(phrase)
        else:
            print("That was all the phrases")


if __name__ == "__main__":
    main()