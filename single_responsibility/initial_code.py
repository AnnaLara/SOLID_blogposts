import random

# This is the path for Mac. Windows and Linux OS have a different path for dictionary
word_file = "/usr/share/dict/words"
words = open(word_file).read().splitlines()

# Generate random word that contains 6 characters or more
random_word = ''
while len(random_word) < 6:
    random_word = random.choice(words).lower()

# Define the main function
def guess_word(word):
    '''Play Guess the Word Game '''
    guessed_w = '*' * len(word)
    
    letters_tried = []
    
    print('Guess the word! ', guessed_w)
    
    while guessed_w != word:
        letter = input("Guess a letter: ").lower()
        
        if letter in letters_tried:
            print('You have already tried this letter! Try another')
        else:
            letters_tried.append(letter)
            
            if letter in word:
                positions = [pos for pos, char in enumerate(word, 0) if char == letter]
                
                for i, char in enumerate(guessed_w):
                    if i in positions:
                        #print(i)
                        array = [char for char in guessed_w]

                        array[i] = letter

                        guessed_w = ''
                        for n in array:
                            guessed_w += n

                    
                print('You guessed right! ', guessed_w)
            else:
                print('There is no such letter in the word')
            
        
    print('You guessed the word! It is ', guessed_w)
    
# Call the function to play the game
guess_word(random_word)