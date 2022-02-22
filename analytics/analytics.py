# Find the best 5-letter words to start with in Wordle

# TODO: 
# x. Top 10 most greens list
# x. Top 10 most anys list
# 3. find most common 2,3,4-letter combos
# 4. what % of 'oo' and 'ee' words are excluded

from collections import Counter
import time

def load_words(filepath):
    with open(filepath) as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def make_letter_count_dict(words):
    """
    Returns a Counter dictionary with number of letter occurrences in 'words'.
    Doubles like 'oo' in 'woods' only count once.
    """
    d = Counter() # counts frequency of letters in all 5 letter words

    for word in words:
        for letter in set(word):
            d[letter] += 1
    
    return d

def make_letter_loc_count_dict(words, loc):
    """
    Counts letter occurrences in a location (0,1,2,3,4)
    """
    d = Counter() # counts frequency of letters in all 5 letter words

    for word in words:
        d[word[loc]] += 1
    
    return d

def count_green(word, dicts):
    # returns integer, number of greens the word gets assuming it sees every word once
    # apply this to word list then rank
    # dicts is a dictionary containing five counter dictionaries; 
    # d0,d1,d2,d3,d4
    # items in the dicts are tuples (letter, count)
    count = 0
    for d,letter in zip(dicts, word):
        count += d[letter]
    
    return count

def count_any(word, d):
    count = 0
    for letter in word:
        count += d[letter]
    
    return count

if __name__ == '__main__':
    wordle_words = load_words('game/word_lists/wordle-answers-alphabetical.txt')
    print(f"Number of Wordle words: {len(wordle_words)}")

    #startTime = time.time()

    d = make_letter_count_dict(wordle_words)
    
    for x in d.most_common():
        print(x)
    
    # create dictionaries for letter occurrences for each position
    dicts = {}
    for i in range(0,5):
        print("------------------------------------")
        dicts[f'd{i}'] = make_letter_loc_count_dict(wordle_words, i)
        print(f"LETTER NUMBER {i+1}:")
        print(dicts[f'd{i}'])

    # fill a counter dictionary for greens and anys
    green_counter = Counter()
    any_counter = Counter()
    for word in wordle_words:
        if len(word) == len(set(word)): # don't want to start with a word with duplicate letters
            green_counter[word] += count_green(word, dicts.values())
            any_counter[word] += count_any(word, d)
        
    # list top 20 green with 5 different letters
    top_ten_green = green_counter.most_common()[0:20]
    print("GREEN RANKINGS")
    for i,word in enumerate(top_ten_green):
        print(f"{i}. {word}")
    
    # list top 20 any (green or yellow)
    top_ten_any = any_counter.most_common()[0:20]
    print("ANY RANKINGS")
    for i,word in enumerate(top_ten_any):
        print(f"{i}. {word}")

    # what % of 'oo' and 'ee' get removed in Wordle list vs. Scrabble list?
    scrabble_words = load_words('words_alpha.txt')
    five_letter_words = { word for word in scrabble_words if len(word) == 5 }
    n = len(five_letter_words)
    print(f"Number of 5-letter Scrabble words: {n}")

    oo_count_wordle = 0
    oo_count_scrabble = 0
    ee_count_wordle = 0
    ee_count_scrabble = 0
    oo_nos_wordle = 0
    oo_nos_scrabble = 0
    ee_nos_wordle = 0
    ee_nos_scrabble = 0
    for word in wordle_words:
        if 'oo' in word:
            oo_count_wordle += 1
            print(word)
            if word[-1] != 's':
                oo_nos_wordle += 1
        if 'ee' in word:
            ee_count_wordle += 1
            print(word)
            if word[-1] != 's':
                ee_nos_wordle += 1
    for word in scrabble_words:
        if 'oo' in word:
            oo_count_scrabble += 1
            if word[-1] != 's':
                oo_nos_scrabble += 1
        if 'ee' in word:
            ee_count_scrabble += 1
            if word[-1] != 's':
                ee_nos_scrabble += 1


    
    print(f"Number of 'oo' in Wordle: {oo_count_wordle}. {oo_count_wordle - oo_nos_wordle} of them end in 's'")
    print(f"Number of 'oo' in Scrabble: {oo_count_scrabble}. {oo_count_scrabble - oo_nos_scrabble} of them end in 's'")
    print(f"Number of 'ee' in Wordle: {ee_count_wordle}. {ee_count_wordle - ee_nos_wordle} of them end in 's'")
    print(f"Number of 'ee' words in Scrabble: {ee_count_scrabble}. {ee_count_scrabble - ee_nos_scrabble} of them end in 's'")
        


        

    #executionTime = (time.time() - startTime)
    #print('Execution time in seconds: ' + str(executionTime))
    
        
