from game.card import Card

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
        """Constructs a new Player.
        
        Args:
            self (Player): an instance of Player.
        """
        self.card = []
        self.score = 300
        self.is_playing = True

        for i in range(2):
            card = Card()
            self.card.append(card)


    def start_game(self):
        """This is the main structure for the game to run. it will start the game, calling the 
        functions do_uptade, get_input, and do_output. It also control the loop game.
        """
        while self.is_playing:
            self.do_updates()
            self.get_input()
            self.do_output() 

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        self.card_values = []
        print('------------------------------')
        for i in range(len(self.card)):
            card = self.card[i]
            card.play()
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
        print(f"Next card was: {self.card_values[1]}")
        print(f"Score is: {self.score}")
        self.continue_playing(self.score)
        
    def continue_playing(self, score):        
        """ask if the player wants to continue playing

        Args:
            self (Director): An instance of Director.
            score (int): The score for the entire game.
        """
        play_again = ""
        if score > 0: 
            play_again = input("play again?[y/n] ")
            if (play_again == "no" or play_again == "n") : 
                print(f'\n***Thanks for playing your score is: {self.score}***')
                self.is_playing = False
            elif (play_again == "y" or play_again == "yes"): 
                self.is_playing = True
            else: 
                False
                
        elif score <= 0 :
            self.is_playing = False
            print(f'Thanks for playing your score is: {self.score}')
      
