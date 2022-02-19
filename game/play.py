# Play a game of Wordle from the command line

# TODO: print out letters that are not in the word
# xxx reject invalid 5-letter guesses

from random import sample

WORD_LIST_FILEPATH = 'word_lists/wordle-answers-alphabetical.txt'
GUESS_LIST_FILEPATH = 'word_lists/wordle-allowed-guesses.txt' # doesn't include words from WORD_LIST_FILEPATH

class Wordle:    
    def __init__(self):
        self.game_state = { letter: '_' for letter in letters }
        self.guessed_letters = set()
        self.guessed_words = []
        self.results = []
    
    def play(self):
        """
        Run loop of get_secret_word -> ask_player_for_guess ->
        evaluate_guess -> display_letter_list until secret_word is guessed
        """

        secret_word = self.get_secret_word(WORD_LIST_FILEPATH)
        is_correct = False

        while not is_correct:
            guess = self.ask_player_for_guess(GUESS_LIST_FILEPATH, WORD_LIST_FILEPATH)
            is_correct = self.evaluate_guess(secret_word, guess)
            self.display_letter_list()
            for guess, result in zip(self.guessed_words, self.results):
                print(f"{guess}: {result}")
            print("____________________________________________________")
        
        print("Congratulations! You guessed the secret word!")
    
    def get_secret_word(self, word_list_filepath):
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
        Prints out the square clues and updates the game_state.
        Returns True if guess = secret_word else False
        """
        if guess == secret_word:
            return True 

        result = ""
        for secret_letter, guessed_letter in zip(secret_word, guess):
            # display clues
            if secret_letter == guessed_letter:
                result += 'g'
            elif guessed_letter in secret_word:
                result += 'y'
            else:
                result += '_'

            # update game state and guessed letter list
            if guessed_letter not in secret_word:
                self.game_state[guessed_letter] = 'x'
            elif self.game_state[guessed_letter] in ['g', 'x']: # 'g' and 'x' are final states
                continue
            elif self.game_state[guessed_letter] == 'y': # already guessed letter but in wrong spot
                if secret_letter == guessed_letter:
                    self.game_state[guessed_letter] == 'g'
            elif guessed_letter == secret_letter:
                self.game_state[guessed_letter] = 'g'
            elif guessed_letter in secret_word:
                self.game_state[guessed_letter] = 'y'
            else: # letter hasn't been guessed yet, isn't 'g', and isn't 'y'
                self.game_state[guessed_letter] = 'x'

            self.guessed_letters.add(guessed_letter)

            self.verify_game_status(secret_word)
        
        print(result)

        self.guessed_words.append(guess)
        self.results.append(result)

        return False

    def display_letter_list(self):
        """
        Displays an alphabet (or keyboard) indicating which letters
        have been guessed, and which guessed letters are in the secret_word
        """
        for k,v in self.game_state.items():
            print(f'{k}: {v}')

    def verify_game_status(self, secret_word):
        """
        Makes sure game state is correct after being updated
        """
        pass

if __name__ == "__main__":
    num_won = 0
    again = 'y'
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #initial_game_state = { letter: '_' for letter in letters }

    w = Wordle()

    while again == 'y':
        w.play()
        num_won += 1
        again = input("Play again? (y/n) ").lower()
    
    print(f"Game over. You won {num_won} games!")
