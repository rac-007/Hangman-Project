'''
The import random loads the random module, 
which contains a number of random number generation-related functions.
'''
import random

'''
Randomly generating a word from a given list of words.
The 'word' will hold the randomly generated value 
'''
if __name__ == "__main__":
    word_list = ["peach","banana","orange","plum","melon"]
    print(word_list)
    word = random.choice(word_list)

    #print(word)
    '''
    Asking for user input and checking for valid input value
    '''

    guess = str(input("Please enter a single letter:"))
    if len(guess)==1 and guess.isalpha():
        print("Good Guess!")
    else:
        print("Oops! That is not a valid input.")    