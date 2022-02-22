from classes.wordle import Wordle
from classes.solver import Solver
from utils import get_secret_word, play_again

WORD_LIST_FILEPATH = 'word_lists/wordle-answers-alphabetical.txt'
GUESS_LIST_FILEPATH = 'word_lists/wordle-allowed-guesses.txt' # doesn't include words from WORD_LIST_FILEPATH
USED_WORDS_FILEPATH = 'word_lists/used.txt'

if __name__ == "__main__":
    w = Wordle()
    s = Solver()

    again = True
    while again:
        secret_word = get_secret_word(WORD_LIST_FILEPATH, USED_WORDS_FILEPATH)
        is_correct = False
        while not is_correct: # game loop
            # end game if player fails on 6th guess
            if w.guess_count > 5:
                print(f"Game over. The secret word was {secret_word}")
                break
            a = input("Would you like a solver recommendation? (y/n) ")
            if a.lower() == 'y':
                with open(WORD_LIST_FILEPATH) as f:
                    # TODO: the solver changes to the game state are persisting for some reason
                    rec = s.solve(w.game_state, set(f.read().split()))
                    print(f"Recommended guess: {rec}")
            # For each
            guess = w.ask_player_for_guess(GUESS_LIST_FILEPATH, WORD_LIST_FILEPATH)
            # end game if player entered 'q' or 'quit'
            if guess in ['Q', 'QUIT']:
                print(f"Game over. The secret word was {secret_word}")
                break
            w.guess_count += 1
            is_correct = w.evaluate_guess(secret_word, guess)
            if is_correct:
                print(f"Congratulations! You guessed the secret word {secret_word}!")
                break
            # display game state
            for k,v in w.game_state.items():
                print(f"{k}: {v}")
            for i, (guess, result) in enumerate(zip(w.guessed_words, w.results)):
                print(f"({i+1}) {guess}: {result}")
            print("____________________________________________________")
        again = play_again()
        w.reset_game_state()
    print(f"Game over. You won {w.num_won} games!")

