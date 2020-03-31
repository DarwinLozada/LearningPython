from random import shuffle


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.number, self.suit)


class Player:
    def __init__(self, name, puntuation):
        self.name = name
        self.puntuation = puntuation


class Game:
    def __init__(self, players):
        self.players = players

    def start_game(self):
        pass

    def determinate_winner(self):
        pass


class Deck:
    suits = ["Diamonds", "Spades", "Clubes", "Hearts"]
    max_number = 13

    def __init__(self):
        self.cards = []

        for suit in self.suits:
            for number in range(1, self.max_number + 1):
                self.cards.append(Card(number, suit))

    def give_random_card(self):
        try:
            if self:
                i = shuffle(self)
                return i[0]
        except IndexError:
            print("The list has no elements")

    def __str__(self):
        return "Mazo de {} cartas".format(len(self.cards))


if __name__ == "__main__":
    deck = Deck()
    print(deck)
