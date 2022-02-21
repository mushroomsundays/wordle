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