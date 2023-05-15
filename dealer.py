from human import Human

# Dealer is inherited from Human
class Dealer(Human):
    def __init__(self, name):
        super().__init__( name)
