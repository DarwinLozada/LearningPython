from random import choice
from time import sleep

REST_TIME = 1
happy_quotes = ["Every day is a new day.", "The purpose of our lives is to be happy.",
                "Embrace the glorious mess that you are.",
                "Being happy never goes out of style.",
                "Happiness is the best makeup.",
                "The mere sense of living is joy enough.",
                "The only thing that will make you happy is being happy with who you are."]

furniture = ["Office chair", "Desk", "Bookshelf", "Table lamp", "Stool",
             "Bench", "Sofa", "Armchair"]

drinks = ["Cola drink", "Coffe", "Chocolate", "Beer", "Wine", "Juice",
          "Iced tea", "Water"]

hate_quotes = ["It is easy to hate and it is difficult to love.",
               "From the deepest desires often come the deadliest hate."
               "Hating people is like burning down your own house to get rid of a rat",
               "Hate cages all the good things about you.",
               "Hate is like water in a dry gulch. The longer it runs, the deeper it digs."]

foods = ["Chicken", "Fish", "Eggs", "Rice", "Peanut", "Tomato", "Bread", "Soup"
                                                                         "Corn", "Meat" "Cookie", "Arepa", "Burger",
         "Pizza", "Ice cream", "Beans"]

absurd_phrases = ["A First Sign of the Beginning of Understanding is the Wish to Die.",
                  "Religion. It's given people hope in a world torn apart by religion.",
                  "Beauty is a whore, I like money better",
                  "When all else fails, there's always delusion."]

animals = ["Dog", "Cat", "Bunny", "Kanguroo", "Bird", "Hamster", "Frog", "Horse"
                                                                         "Parrot", "Goat", "Rat", "Snake", "Duck"]

motivational_quotes = ["Your limitation—it’s only your imagination.",
                       "Sometimes later becomes never. Do it now.",
                       "Dream it. Wish. Do it.",
                       "Dream bigger. Do bigger.",
                       "Do something today your future self will thank you for",
                       "Little things make big days."]

animal_sounds = ["Wof wof", "Kii-kiki-ri-ki", "Meow- meow", "Cuack-cuack", "Oink-oink",
                 "Moo-moo"]

sad_quotes = ["It's okay to be sad if things don't go the way you had hoped.",
              "Everything takes me longer than I expect. It's the sad truth about life.",
              "Tears are words that need to be writtin.",
              "We must understand that sadness is an ocean, and sometimes we drown, while other days we are forced to"
              "There is no greater sorrow than to recall in misery the time when we were happy."]


def choosefromlist(list_from):
    print(choice(list_from))
    sleep(REST_TIME)


def main():
    frases = [happy_quotes, furniture, drinks, hate_quotes, foods, absurd_phrases, animals, motivational_quotes,
              animal_sounds, sad_quotes]

    for number in range(200):
        last_number = int(str(number)[-1])
        print(number, choice(frases[last_number]))
        sleep(2)


if __name__ == "__main__":
    main()
