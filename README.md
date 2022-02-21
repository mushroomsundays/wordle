Run `play.py` to play a game of Wordle in the terminal.

The secret word is chosen randomly from the official Wordle word list, then stored in word_lists/used.txt. Used words are not re-used.

Legend:
'g': correct letter, correct spot
'y': correct letter, wrong spot
'_': letter is not in secret word

After 6 incorrect guesses, the game ends and the secret word is revealed.

The user can give up by entering 'q' or 'quit' when prompted for a guess.

Upcoming:
1. Recommendation engine (solver)
2. Username + password log in
