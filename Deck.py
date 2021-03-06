 class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q","K"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual_cards = min([count,num])
        if count == 0:
            raise ValueError("All cards have been dealth")
        card = self.cards[-actual_cards:]
        self.cards = self.cards[:-actual_cards]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
