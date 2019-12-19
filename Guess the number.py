import random
from time import sleep


def main():

    while True:
        random_number = random.choice(range(10))
        guess = int(input("Guess a number between 0 and 10 "))
        if guess == random_number:
            print("Congrats! that was {}".format(random_number))
        else:
            print("Nope, that wasn't the number")
        sleep(3)


if __name__ == "__main__":
    main()
