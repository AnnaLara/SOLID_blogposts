
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
