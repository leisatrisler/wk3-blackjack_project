# Card Class
class Card:
    def __init__(self, card_suit, card_type, card_value) :
        ''''''
        self.card_suit = card_suit
        self.card_type = card_type
        self.card_value = card_value

    def which_card(self):
        return self.card_suit