from random import sample

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

def play_again():
    """Returns True if yes, False if no. Prompts user on invalid input"""
    valid_input = False
    while not valid_input:
        _input = input("Play again? (y/n) ").lower()
        if _input in ['y', 'Y', 'n', 'N']:
            if _input.lower() == 'n':
                return False 
            else:
                return True
        else:
            print("Please enter 'y' or 'n'")
