import random

# TODO: Implement the Card class as follows...
class Card:

    
# 1) Add the class declaration. Use the following class comment.
    """Random Cards valued between 1 and 13

    The responsibility of Card is to provide a random card. 
   
    Attribute:
        card (int): The first random card provided
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Card with a value (0) attribute.

        Args:
            self card (Card): An instance of Card.
            
        """
        self.card=0

# 3) Create the random(self) method. Use the following method comment.
    """Generates a new random value between 1 and 13. 
        
    Args:
        self card (Card): An instance of Card.
        
    """
    def play(self):
        
        self.card = random.randint(1, 13) 

       
