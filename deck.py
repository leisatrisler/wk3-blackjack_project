import random
import card as c


class Deck:
    def __init__(self):
        self.cards = []
        self.build_new_deck()
        
    def build_new_deck(self):

        card_suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        card_types= ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        card_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

        for suit in card_suit: # For Loop Iterates four times over cards over line 13
            for t in card_types: # sub loop aka nested looped within the card_suit using card_types
                self.cards.append(c.Card(suit, t, card_values[t])) # t is for type but its protected
        return self.cards
    
    def randomize_cards(self):
        '''Shuffle Cards'''
        random.shuffle(self.cards)

    def deal_card(self):
        '''get and remove a card from the deck '''
        return self.cards.pop()
    
    
    def get_cards(self):
        '''return array of cards'''
        return self.cards




# class Deck:
#     def _deck_(self, deck_hand, card, card_value):
#         for card_type in card_types:
#             ["Clubs", "Diamonds", "Hearts", "Spades"]

# card_values = ["Clubs", "Diamonds", "Hearts", "Spades"]
# card = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# card_value = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

# for card in card: 
#     if ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:  
#         if card.append(Card(card_values[card], card, card[card])): # shuffle?
#             while: deck_hand > (21):
#                 return:(Bust)
#         elif: (deck_hand) < (21)
      

