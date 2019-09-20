def read_file(file):
    '''Read file'''
    return open(file,"r").read()

def number_of_words(file):
    '''Count number of words in a file'''
    f = read_file(file)
    return len(f.split())

def count_word(word, file):
    '''Count numer of word occurrences in a file'''
    t = read_file(file)
    counter = 0
    for e in t.split():
        if word.lower() == e.lower():
            counter +=1
    return counter

def percentage_of_word(word, file):
    '''Calculate ratio of number of word occurrences to number of all words'''
    total_words = number_of_words(file)
    word_occurrences = count_word(word, file)
    return word_occurrences/total_words