import random
from words import words
import string # a builtin library for ASCII letters and methods

# valid word selection function from words list
def get_valid_word(words):
    word = random.choice(words) #it will randomlly itrates over words list and chooses a random word from list
    while '_' in word or ' ' in word: #used while loop to tell that word should not have a '_' or empty space ' '
        word = random.choice(words)

    return word.upper() #and when there will be a word without empty space or underscore it will return that word with uppercase


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet  = set(string.ascii_uppercase) #to generate uppercase alphabets
    used_letters = set() # an empty set to keep track of the alphabets we already used

    lives = 6
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # Leters used
        # ' '.join(['a', 'b', 'cd'])---> 'a b cd'
        print('you have',lives, 'lives left and You have used these letters: ', ''.join(used_letters))
        
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ''.join(word_list))


        user_letter = input('Guess a Letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # takes away a life if wrong guess
                print('Letter is not in the word.')

        elif user_letter in used_letters:
            print("you have already used that character, Please try again.")

        else:
            print('Inavalid Character. Please try again')

    # get here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You Died, sorry, The word was', word)
    else:
        print('Wow you guessed the word', word)
hangman()

# user_input = input('Type something: ')
# print(user_input)