

class Solver:
    """
    1. Input game state
    2. Read in wordle answer list
    3. map(calculate_answer_space) to every remaining word and recommend lowest result
    4. 
    """
    def __init__(self):
        """
        Maybe don't even need to store recommendations; we just get the game
        state from the Wordle object
        """
        pass 

    def solve(self):
        """
        Maps calculate_answer_space onto entire word list, and returns the one
        with the smallest answer space.
        """
        pass 

    def calculate_answer_space(self, game_state, word):
        """
        Plays the word in the current game state and calculates how many
        words are valid after that, on average.
        Need to play this out for every word remaining in the list

        To get answer space: Checks is_valid_answer for every remaining 
        word in the list, and returns 
        """
        pass

    def is_valid_answer(self, game_state, word):
        """
        Returns true if 'word' is a valid answer given 'game_state'
        """
        pass
