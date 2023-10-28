## Task 1: Iteratively check if the input is a valid guess

# guess = None
word = "piffle"
# 
# while True:
#     guess = input("Please input a letter: ")
#     
#     if len(guess) == 1 and guess.isalpha() == True : break
#     else : print("Invalid letter. Please, enter a single alphabetical character.")

## Task 2: Check whether guess is in the word

# if guess in word : print(f"Good guess! {guess} is in the word.")
# else : print(f"Sorry, {guess} is not in the word. Try again.")

## Task 3: Create functions to run the checks

def check_guess(guess):
    """Check if the guessed letter is in the word."""
    guess = guess.lower()
    
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    """Prompt the user for a letter and check if it's in the word."""
    guess = None

    while True:
        guess = input("Please input a letter: ")
        
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)
    return guess

ask_for_input()