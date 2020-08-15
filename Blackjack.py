from random import shuffle

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11,
          "Queen": 12, "King": 13, "Ace": 14}

class Deck:

    def __init__(self):
        self.all_cards = [Card(s, r) for s in suits
                                     for r in ranks]

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Hand:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} cards"

    def __len__(self):
        return len(self.all_cards)

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

deck = Deck()
house = Hand("House")
player1 = Hand(input("Please enter your name: "))
house.add_cards([deck.deal_one(), deck.deal_one()])
player1 = ([deck.deal_one(), deck.deal_one()])
