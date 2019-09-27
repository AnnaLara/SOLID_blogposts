
def percentage_of_word(search, file):
    search = search.lower()
    content = open(file, "r").read()
    words = content.split()
    number_of_words = len(words)
    occurrences = 0
    for word in words:
        if word.lower() == search:
            occurrences += 1
    return occurrences/number_of_words


def count_word_occurrences(word, localfile):
    content = return open(file, "r").read()
    counter = 0
    for e in content.split():
        if word.lower() == e.lower():
            counter += 1
    return counter
