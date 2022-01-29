 
 
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
        self.card_values = []
        print('------------------------------')
        for i in range(len(self.card)):
            card = self.card[i]
            card.shuffle()
            self.card_values.append(card.value)
        self.card_values = [int(i) for i in self.card_values]
        print(f"\nThe card is {self.card_values[0]}")

    def get_input(self):
        """Ask the user if the card is higher or lower, and give score

        Args:
            self (Director): An instance of Director.
        """
        answer = input("Higher or lower? [h/l] ")
        if answer == 'h':
            if self.card_values[1] > self.card_values[0]:
                self.score += 100 
            else:
                self.score -= 75 
        elif answer == 'l':
            if self.card_values[1] < self.card_values[0]:
                self.score += 100 
            else:
                self.score -= 75


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
