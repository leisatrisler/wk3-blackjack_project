class Human:
    '''human class for player and dealer'''

    def __init__(self, name):
        self.name = name
        self.hand_dealt = []

    def add_card(self, card):
        self.hand_dealt.append(card)

    def hit(self, card):
        self.hand_dealt.append(card)

    def stand(self):
        '''do nothing'''
        pass

    def get_hand_value(self):
        total = 0
        aces = 0
        for card in self.hand_dealt:
            if str(card.card_value).isdigit():
                total += int(card.card_value)
            elif card.card_value in ['j', 'q', 'k']:
                total += 10
            elif card.card_value == 'a':
                aces += 1
                total += 11
            while total > 21 and aces > 0:
                total -= 10
                aces -= 1
        return total

    def show_hand(self, show_all_cards=False):
        print(f"{self.name}'s hand:")
        if show_all_cards:
            for card in self.hand_dealt:
                print(f"{card.card_value} of {card.card_suit}")
        else:
                print("Card Not Visable")


            