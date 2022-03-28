
##################################################################################################################################################
##### Implementing Hangman where the user guesses a word, which is selected from a large list of words by the computer, through the ue of loops####
##################################################################################################################################################

import random 
from words import words
import string

def get_valid_word(words):             # Function to select a random valid word to be used in hangman

    word = random.choice(words)

    while '-' in word or ' ' in word:  # We select a word which is a single, non-hyphenated word
        word = random.choice(word)

    return word.upper()

def hangman():

    # Initial Set Up of Game

    word = get_valid_word(words)                    # computer chooses a word to be guessed
    word_letters = set(word)                        # set of unique letters belonging to the word
    alphabets = set(string.ascii_uppercase)         # all characters which can be guessed by user
    used_letters = set ()                           # all characters already guessed by the user

    
    lives = 6    

    
    while len(word_letters) > 0 and lives > 0:

        # showing the used letters : 
        print('You have {} lives left'.format(lives),'\nYou have used these letters : ' , ' '.join(used_letters))# ' '.join(['a', 'b', 'cd']) --> 'a b cd'

        # what the current word is (ie W _ R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]          # ie if letter is gussed, it shows up, otherwise remains blank
        print('\nCurrent Word : ', ' '.join(word_list))

        # Getting User Input
        user_letter = input('Guess a letter : ').upper()

        if user_letter in alphabets - used_letters:
            
            used_letters.add(user_letter)            
            if user_letter in word_letters: 
                word_letters.remove(user_letter)
            else: 
                print('\nYour letter {} is not in the word.'.format(user_letter))
                lives -= 1 # takes away one life if wrong letter is guessed

        elif user_letter in used_letters:
            print('You have already guessed that letter, try another one.')

        else:
            print('Invalid Character')


    #gets here when len(word_letters) == 0 
    if lives == 0:
        print('Game Over. You ran out of lives \n The word was : {}'.format(word))
    else:
        print('Yay! You guessed the word \'{}\' right!'.format(word))

hangman()