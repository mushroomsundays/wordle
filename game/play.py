from classes.wordle import Wordle
from classes.solver import Solver
from utils import get_secret_word, evaluate_play_again

WORD_LIST_FILEPATH = 'word_lists/wordle-answers-alphabetical.txt'
GUESS_LIST_FILEPATH = 'word_lists/wordle-allowed-guesses.txt' # doesn't include words from WORD_LIST_FILEPATH
USED_WORDS_FILEPATH = 'word_lists/used.txt'

if __name__ == "__main__":

    again = True
    w = Wordle()

    while again:
        secret_word = get_secret_word(WORD_LIST_FILEPATH, USED_WORDS_FILEPATH)
        is_correct = False
        while not is_correct: # game loop
            # end game if player fails on 6th guess
            if w.guess_count > 5:
                print(f"Game over. The secret word was {secret_word}")
                break
            # TODO: ask if user wants solver recommendation here
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
            w.display_letter_list()
            for guess, result in zip(w.guessed_words, w.results):
                print(f"{guess}: {result}")
            print("____________________________________________________")
        again = evaluate_play_again()
        w.reset_game_state()
    print(f"Game over. You won {w.num_won} games!")

