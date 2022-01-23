 
 
 #player:
 #Object: player
 """A person who plays the game. 
    
    The responsibility of a player is to get cards each time is the turn to play.

    Behavior:
    
        decide if the next card will be a lower value or will be a higher value than the card shown.

    Attributes:
        
        desition (boolean L/H): the player decide if the turn is for Low or for High card value.
        outcomes (List[win, lose]): depending of the outcomes.
        earn points (int): The points earned for one round of play.
        lose points (int) The points lost for one round of play.
        total_score (int): The score for the player in the entire game.
        finish the game (boolean): the player decide Y/N to play.

    Methods names:
        def ask_for_a_card(self)
        def desition(self)
        def decide_to_continue_playing(self)
        def close(self)


    """
