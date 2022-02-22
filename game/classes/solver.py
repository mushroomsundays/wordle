from collections import defaultdict
from email.policy import default

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

    def solve(self, game_state, word_list):
        """
        Loop through each word in word list, and calculate answer space
        *after* that word has been played. 
        Store results in dictionary, then choose lowest answer space
        """

        d = defaultdict()
        for word in word_list:
            word = word.upper()
            new_game_state = game_state.copy() # game state will bloat without .copy(); Python never implicitly copies
            #print("---------solve()----------")
            #print(f"Word: {word}")
            if self.is_valid_answer(game_state, word):
                #print("FRESH GAME STATE")
                #for k,v in new_game_state.items():
                    #print(f"{k}: {v}")
                # update game state after current word is guessed, assuming none of the letters hit
                for letter in word:
                    if game_state[letter] == '_':
                        new_game_state[letter] = 'x'
                #print(f"GAME STATE AFTER {word}")
                #for k,v in new_game_state.items():
                    #print(f"{k}: {v}")
                d[word] = self.calculate_answer_space(new_game_state, word_list)
        #print(f"Words remaining: {len(d.keys())}")
        #print("Word: Answer space size")
        for k,v in d.items():
            print(f"{k}: {v}")
            
        return min(d, key=d.get).upper()

    def calculate_answer_space(self, game_state, word_list):
        """
        To get answer space: Checks is_valid_answer for every remaining 
        word in the list, and returns the number of possible answers remaining
        """
        # 1. update game_state with each possible word
        # 2. count number of is_valid_answer from that game state and return it
        for word in word_list:
            word = word.upper()
            new_game_state = game_state.copy()
            for letter in word:
                if game_state[letter] == '_':
                    new_game_state[letter] = 'x'
            valid_words = { word for word in word_list if self.is_valid_answer(new_game_state, word) }

        return len(valid_words)

    def is_valid_answer(self, game_state, word):
        """
        Returns true if 'word' is a valid answer given 'game_state'
        game_state is a dict {A: 'g', B: '_', ....}
        """
        #("--------is_valid_answer()---------")
        #print(f"Word: {word}")
        # check that game_state is compatible
        for letter,status in game_state.items():
            letter = letter.upper()
            if status == 'x':
                if letter in word:
                    #print(f"{letter} is in {word} but {letter} has 'x' status")
                    return False 
            elif status == 'g':
                if letter not in word:
                    #print(f"{letter} is not in {word} but {letter} has 'g' status")
                    return False 
            elif status == 'y':
                if letter not in word:
                    #print(f"{letter} is not in {word} but {letter} has 'y' status")
                    return False
        # check that letters are in correct spot
        for letter in word:
            letter = letter.upper()
            letter_status = game_state[letter]
            if letter_status == 'x':
                #print(f"{letter} is in {word} but {letter}'s status is 'x'")
                return False
            elif letter_status == 'y':
                if letter not in word:
                    #print(f"{letter} is not in {word} but {letter}'s status is 'y'")
                    return False 
        
        return True
