import random

# TODO: Implement the Card class as follows...
class Card:

    
# 1) Add the class declaration. Use the following class comment.
    """Random Cards valued between 1 and 13

    The responsibility of Card is to provide and display random card on screen. 
   
    Attributes:
        card (int): The first random card provided
        next_card (int): The second random card provided
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Card with a value (0) attribute.

        Args:
            self card (Card): An instance of Card.
            self next_card (Card): Another instance of Card.
        """
        self.card=0
        self.next_card=0    

# 3) Create the random(self) method. Use the following method comment.
    """Generates a new random value, display it on screen and then ask the player if the next card will be higher or lower.
        
    Args:
        self card (Card): An instance of Card.
        self next_card (Card): Another instance of Card.
    """
    def play(self):
        #This code is just the beginning...
        self.card = random.randint(1, 3) 
        print(f"The card is: {self.card}")
        #Choice variable will be used to check one of the game conditions. 
        choice = input("The number will be higher or lower? h/l ")
        self.next_card = random.randint(4,13)
        print(f"Next card was: {self.next_card}")
