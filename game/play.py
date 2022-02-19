# Play a game of Wordle from the command line

# TODO: print out letters that are not in the word
# xxx reject invalid 5-letter guesses

from random import sample

WORD_LIST_FILEPATH = 'word_lists/wordle-answers-alphabetical.txt'
GUESS_LIST_FILEPATH = 'word_lists/wordle-allowed-guesses.txt' # doesn't include words from WORD_LIST_FILEPATH

class Wordle:
    
    # instance attributes
    def __init__(self):
        pass
    
    # instance methods
    def play(self):
        """
        Run infinite loop of get_secret_word -> ask_player_for_guess ->
        evaluate_guess until 
        """

        secret_word = self.get_secret_word(WORD_LIST_FILEPATH)
        is_correct = False

        while not is_correct:
            guess = self.ask_player_for_guess(GUESS_LIST_FILEPATH, WORD_LIST_FILEPATH)
            is_correct = self.evaluate_guess(secret_word, guess)
            self.display_letter_list()
        
        print("Congratulations! You guessed the secret word!")
    
    def get_secret_word(self, word_list_filepath):
        """Picks a word for a new_game"""
        with open(word_list_filepath) as f:
            word_list = set(f.read().split())
            x = sample(word_list, 1).pop().upper()
        
        return x

    def ask_player_for_guess(self, guess_list_filepath, word_list_filepath):
        """
        Ask the player for a five letter word. If the word is not valid,
        prompt the player for a new word until they enter a valid one.
        """
        is_valid = False 
        while not is_valid:
            x = input("Enter a five letter word: ")

            with open(guess_list_filepath) as f1, open(word_list_filepath) as f2:
                valid_guesses = set(f1.read().split()).union(set(f2.read().split()))
                if x.lower() in valid_guesses:
                    is_valid = True
                elif x.isalpha() and len(x) == 5:
                    print("Word not found in word list, try again...")
                else:
                    print("Invalid input, try again...")

        return(x.upper())

    def evaluate_guess(self, secret_word, guess):
        """
        Prints out the square clues.
        Returns True if guess = secret_word else False
        """
        if guess == secret_word:
            return True 

        result = ""
        for secret_letter, guessed_letter in zip(secret_word, guess):
            if secret_letter == guessed_letter:
                result += 'g'
            elif guessed_letter in secret_word:
                result += 'y'
            else:
                result += '_'
        
        print(result)

        return False

    def display_letter_list(self):
        """
        Displays an alphabet (or keyboard) indicating which letters
        have been guessed, and which guessed letters are in the secret_word
        """
        pass

if __name__ == "__main__":
    w = Wordle()
    num_won = 0
    again = 'y'

    while again == 'y':
        w.play()
        num_won += 1
        again = input("Play again? (y/n) ").lower()
    
    print(f"Game over. You won {num_won} games!")
