
from random import sample

WORD_LIST_FILEPATH = 'word_lists/wordle-answers-alphabetical.txt'
GUESS_LIST_FILEPATH = 'word_lists/wordle-allowed-guesses.txt' # doesn't include words from WORD_LIST_FILEPATH
USED_WORDS_FILEPATH = 'word_lists/used.txt'

class Users: 
    def __init__(self):
        self.username = ""
        self.password = ""

    def login():
        """
        Log the user in. User accounts are stored in userx.json
        """
        pass 

    def create_account():
        """
        Let the user enter their username and password. 
        Store credentials in users.json
        """
        pass

def get_secret_word(word_list_filepath, used_words_filepath):
    with open(word_list_filepath) as f1, open(used_words_filepath, 'a') as f2:
        wordle_words = set(f1.read().split())
        try:
            used_words = set(f2.read().split())
        except: # empty file
            used_words = set()

        # remove words that were already used
        usable_words = { word for word in wordle_words if word not in used_words }
        x = sample(usable_words, 1).pop().upper()

        # write used word to word_lists/used.txt
        f2.write('\n')    
        f2.write(x)

    return x

class Wordle:    
    def __init__(self):
        self.game_state = { letter: '_' for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' }
        self.guessed_letters = set()
        self.guessed_words = []
        self.guess_count = 0
        self.results = []
        self.num_won = 0
    
    def play(self):
        """
        Run game loop of get_secret_word -> ask_player_for_guess ->
        evaluate_guess -> display_letter_list until secret_word is guessed
        """

        secret_word = get_secret_word(WORD_LIST_FILEPATH, USED_WORDS_FILEPATH)
        is_correct = False

        while not is_correct:
            # end game if player fails on 6th guess
            if self.guess_count > 5:
                print(f"Game over. The secret word was {secret_word}")
                return

            guess = self.ask_player_for_guess(GUESS_LIST_FILEPATH, WORD_LIST_FILEPATH)

            # end game if player entered 'q' or 'quit'
            if guess in ['Q', 'QUIT']:
                print(f"Game over. The secret word was {secret_word}")
                return

            self.guess_count += 1
            is_correct = self.evaluate_guess(secret_word, guess)
            self.display_letter_list()
            for guess, result in zip(self.guessed_words, self.results):
                print(f"{guess}: {result}")
            print("____________________________________________________")
        
        print(f"Congratulations! You guessed the secret word {secret_word}!")

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
            self.num_won += 1
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

            self.verify_game_state(secret_word)
        
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

    def verify_game_state(self, secret_word):
        """
        Makes sure game state is correct after being updated
        """
        pass

    def reset_game_state(self):
        self.game_state = { letter: '_' for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' }
        self.guessed_letters = set()
        self.guessed_words = []
        self.guess_count = 0
        self.results = []

if __name__ == "__main__":
    """
    # prompt user to log in or create account
    print("Menu")
    print("(1) Log in")
    print("(2) Create account")
    a = input()
    """

    # play Wordle
    again = 'y'
    w = Wordle()

    while again == 'y':
        w.play()
        again = input("Play again? (y/n) ").lower()
        w.reset_game_state()
    
    print(f"Game over. You won {w.num_won} games!")
