# file: ex_08_06_card_deck_start.py
import random

SUITS  = ["Clubs", "Diamonds", "Hearts", "Spades"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
          "Jack", "Queen", "King", "Ace"]

class Card:
    def __init__(self, suit, value):
        # TODO: store _suit and _value
        self._suit = suit
        self._value = value

    def __str__(self):
        # TODO: return e.g. "Ace of Spades"
        return f"{self._value} av {self._suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        self._card = []
        # TODO: create all 52 cards using nested loops over SUITS and VALUES
        for suit in SUITS:
            for value in VALUES:
        # Store them in self._cards as a list
                 self._card.append(Card(suit, value))

    def shuffle(self):
        # TODO: shuffle _cards in place using random.shuffle
         random.shuffle(self._card)

    def draw(self):
        # TODO: remove and return the top card (index 0)
        # Raise IndexError if the deck is empty
        if len(self._card) == 0:
            raise IndexError("Dekk is empty")
        else:
            return self._card.pop(0)

    def __len__(self):
        # TODO: return number of remaining cards
        return len(self._card)

    def __getitem__(self, index):
        # TODO: return card at given index
        return self._card[index]
        

    def __str__(self):
        # TODO: return e.g. "Deck: 52 cards"
        return f"Dekk: {len(self._card)} cards"


if __name__ == "__main__":
    deck = Deck()
    print(f"New deck: {deck}")
    print(f"Top card: {deck[0]}")
    print(f"deck[0]:  {deck[0]}")

    deck.shuffle()
    print(f"\nAfter shuffle - top 5 cards:")
    for i in range(5):
        print(f"  {deck[i]}")

    print(f"\nDrawing 3 cards: ", end="")
    drawn = [str(deck.draw()) for _ in range(3)]
    print(", ".join(drawn))
    print(f"Cards remaining: {len(deck)}")
