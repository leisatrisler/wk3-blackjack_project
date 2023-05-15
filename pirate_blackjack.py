# ## Python Blackjack
# For this project you will make a Blackjack game using Python. Click <a href="http://www.hitorstand.net/strategy.php">here</a> to familiarize yourself with the the rules of the game. You won't be implementing every rule "down to the letter" with the game, but we will doing a simpler version of the game. This assignment will be given to further test your knowledge on object-oriented programming concepts.

# ### Rules:

# `1. ` The game will have two players: the Dealer and the Player. The game will start off with a deck of 52 cards. The 52 cards will consist of 4 different suits: Clubs, Diamonds, Hearts and Spades. For each suit, there will be cards numbered 1 through 13. <br>
# **Note: No wildcards will be used in the program**

# `2. ` When the game begins, the dealer will shuffle the deck of cards, making them randomized. After the dealer shuffles, it will deal the player 2 cards and will deal itself 2 cards from. The Player should be able to see both of their own cards, but should only be able to see one of the Dealer's cards.
 
# `3. ` The objective of the game is for the Player to count their cards after they're dealt. If they're not satisfied with the number, they have the ability to 'Hit'. A hit allows the dealer to deal the Player one additional card. The Player can hit as many times as they'd like as long as they don't 'Bust'. A bust is when the Player is dealt cards that total more than 21.

# `4. ` If the dealer deals the Player cards equal to 21 on the **first** deal, the Player wins. This is referred to as Blackjack. Blackjack is **NOT** the same as getting cards that equal up to 21 after the first deal. Blackjack can only be attained on the first deal.

# `5. ` The Player will never see the Dealer's hand until the Player chooses to 'stand'. A Stand is when the player tells the dealer to not deal it anymore cards. Once the player chooses to Stand, the Player and the Dealer will compare their hands. Whoever has the higher number winsdef shuffle_cards. Keep in mind that the Dealer can also bust. 

# dealer.hit_me(deck)
# player.hit_me(deck)
# dealer.hit_me(deck)
# player.hit_me(deck)

# dealer.stay(deck)
# player.stay(deck)
# dealer.stay(deck)
# player.stay(deck)

# dealer.show_your_hand()
# player.show_your_hand()
# dealer.show_your_hand()
# player.show_your_hand()

from dealer import Dealer
from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck() # Instance Variables 
        self.deck.randomize_cards() # Instance Variables
        self.player = Player("First Mate") # Instance Variables
        self.dealer = Dealer("Captain") # Instance Variables
        self.game_started = False # Instance Variables

    def create_the_deck(self):
        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

    def play(self):
        print("Ahoy Me Hearty, Welcome To Me Ship.") # Game started
        self.game_started = True
        self.create_the_deck()

        player_choice = player_input(game)
        if player_choice.lower() == 'h':
            self.player.add_card(self.deck.deal_card())
            self.player.show_hand(True)
            if self.player.get_hand_value() > 21:
                print("Arr...Walk The Plank, Ye About To Be Marooned") # Busted
                
        player_choice = player_input(game)
        if player_choice.lower() == 'h':
            self.player.add_card(self.deck.deal_card())
            self.player.show_hand(True)
            if self.player.get_hand_value() > 21:
                print("Arr...Walk The Plank, Ye About To Be Marooned") # Busted

        dealer_hand_value = self.dealer.get_hand_value()
        while dealer_hand_value < 17: # Game rule dealer can not pull another if 17 or higher
            self.dealer.add_card(self.deck.deal_card()) 
            dealer_hand_value = self.dealer.get_hand_value()

        self.player.show_hand(True) # Player shows hand
        self.dealer.show_hand(True) # Dealer shows hand

        player_hand_value = self.player.get_hand_value() # Player total of cards
        dealer_hand_value = self.dealer.get_hand_value() # Dealer total of cards

        if player_hand_value > 21:
            print("Arr...Walk The Plank, Ye About To Be Marooned")
        elif dealer_hand_value > 21 or player_hand_value > dealer_hand_value:
            print("Yo-Ho-Ho, It's A Pirate's Life For You")            
        elif player_hand_value < dealer_hand_value:
            print("Blimey! ROPE'S END... Surrender The Booty, All Your Loot Is Now Mine") # Loser
        else:
            print("Dead Mean Tell No Tales, Rematch or Davey Jone's Locker For You") # Tie
            player_input(game)


def player_input(game):
    # if game.game_started is True:
    #     print("Weigh Anchor... Matey") # If rematch in play
    #     game.play()
    #     return
    player_choice = input("Me Hearties. Shall We Gather Some Of thee Booty? (Enter: (y/n) )")
    if player_choice == "n":
        print("Blimey, Ye Scurvy Dog, Ye Abandoned Ship.") # Player Quited Game
        quit()
    elif player_choice == "y":

        player_choice = input("Ye Wish To Hit or Stay, Thee Choice Be Yer's, What Say Ye? Enter: (h/s): ") # Hit or Stay
        choice = player_choice.lower()
        if choice == "h" or choice == "s" or choice == "hit" or choice == "stay": # Hit or Stay
            return player_choice
        else: 
            player_choise = input(f"Avast...Read The Rules Again Matey: [{player_choice}]. Let's Try Again... Enter h/s or hit/stay or quit: ") # If invalid selection
            if (player_choise.lower == "quit"):
                print("Shiver Me Timbers... You Abandoned Ship, You Scallywag.") # Players quit
                quit()
        return player_choise
    


game = Game()
# player_input(game)
game.play()