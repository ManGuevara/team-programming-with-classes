 
 
 #player:


 class Player:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (List[card]): A list of card instances.
        score (int): The score for the entire game.
        is_playing (boolean): Whether or not the game is being played.
        card_values (List[card_value]): A list of Card values
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
    
    def get_input(self):
        """Ask the user if the card is higher or lower, and give score

        Args:
            self (Director): An instance of Director.
        """


    def do_output(self):
        """Displays the the score.and value of the new card 

        Args:
            self (Director): An instance of Director.
        """
     
    def continue_playing(self, score):        
        """ask if the player wants to continue playing

        Args:
            self (Director): An instance of Director.
            score (int): The score for the entire game.
        """
