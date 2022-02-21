from classes.wordle import Wordle

if __name__ == "__main__":

    again = 'y'
    w = Wordle()

    while again == 'y':
        w.play()
        again = input("Play again? (y/n) ").lower()
        w.reset_game_state()
    
    print(f"Game over. You won {w.num_won} games!")

