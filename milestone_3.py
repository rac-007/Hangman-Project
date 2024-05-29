'''
The import random loads the random module, 
which contains a number of random number generation-related functions.
'''
import random
'''
Initializing the list with fruit names in a list variable 'word_list'
'''
word_list = ["peach","banana","orange","plum","melon"]
#print(word_list)

'''
the random.choice() will randomly pick a fruit from the word_list
'''
word = random.choice(word_list)
#print(word)

def check_guess(guess):
    '''
    This method converts the user input into lowercase and checks the passed argument if that is in the 
    randomly generated word.
    This method takes the passed argument 'guess' when called from another method 'ask_for_input'method
    method. Prints meassages according to the condition. 
    '''
    guess_word = guess.lower()
    if guess in word:
        print(f"Great! {guess} is in the secret word. ")
    else:
      print(f"Sorry!this letter {guess} not found in the secret word.")

def ask_for_input():
     '''
     This method takes user input and checks if it is an alphabet.
     '''
     while True:
        guess = str(input("Please enter a letter:"))
        if guess.isalpha()== True:
            print("Good Guess! let us check if this letter is present in the secret word!")
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue        

'''
Calling the method to ask user input.
'''
ask_for_input()