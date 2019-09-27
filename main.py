from functions import percentage_of_word_in_localfile, count_word_occurrences
from functions import get_text_from_url

if __name__ == "__main__":

    # Print out ratio of 'and' occurrences to the total number of words in the 'ufo.txt'
    print(percentage_of_word_in_localfile('and', 'ufo.txt'))

    content = get_text_from_url('https://en.wikipedia.org/wiki/Main_Page')
    count_word_occurrences('and', content)
