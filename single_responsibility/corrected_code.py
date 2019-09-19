import random

def get_random_word(min_length):
    '''Returns a random word with a minimum length'''
    
    # This is the path for Mac. Windows and Linux OS have a different path for dictionary
    word_file = "/usr/share/dict/words"
    words = open(word_file).read().splitlines()
    
    # Generate random word that contains 6 characters or more
    random_word = ''
    while len(random_word) < min_length:
        random_word = random.choice(words).lower()
        
    return random_word
    
def list_to_string(word_list):
    '''Join all the elements in the list into a string'''
    word = ''
    for n in word_list:
        word += n
    return word
    
def string_to_list(word):
    '''Split string into a list of single characters'''
    return [char for char in word]
    
def replace_with_correct_letter(letter, word, guessed_w):
    '''Replace '*' in guessed_w with all the occurances of the letter in word'''
    
    positions = [pos for pos, char in enumerate(word, 0) if char == letter]
                
    for i, char in enumerate(guessed_w):
        if i in positions:
            array = string_to_list(guessed_w)
            array[i] = letter
            guessed_w = list_to_string(array)
           
    return guessed_w

def guess_letter(guessed_w, word, letters_tried):
    letter = input("Guess a letter: ").lower()
        
    if letter in letters_tried:
        print('You have already tried this letter! Try another')
    
    else:
        letters_tried.append(letter)

        if letter in word:
            guessed_w = replace_with_correct_letter(letter, word, guessed_w)

            print('You guessed right! ', guessed_w)
            
        else:
            print('There is no such letter in the word')
    
    return guessed_w



# Define the main function
def guess_word(word):
    '''Play Guess the Word Game '''
    print(word)
    guessed_w = '*' * len(word)
    
    letters_tried = []
    
    print('Guess the word! ', guessed_w)
    
    while guessed_w != word:
        guessed_w = guess_letter(guessed_w, word, letters_tried)            
        
    print('You guessed the word! It is ', guessed_w)
    

# Call the function to play the game
if __name__ == "__main__":
    guess_word(get_random_word(6))