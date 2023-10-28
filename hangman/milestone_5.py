import random as rand
from milestone_4 import Hangman 

def play_game(word_list):
    """
    Initiate and play a Hangman game.
    
    Parameters:
        word_list (list): List of potential secret words to be chosen randomly.
        
    Returns:
        int: 0, to signify the game has ended successfully.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(f"You have now started the hangman game with {num_lives} lives. Enjoy!")

    # Loop through until game has ended
    while True:
        if game.num_lives == 0:
            print(f"You're out of lives! The word was {game.word}.")
            break
        elif '_' not in game.word_guessed:
            print(f"Congratulations! It was {game.word}, you guessed the word!")
            break
        elif game.num_lives > 0:
            game.ask_for_input()
        else:
            print("Something went wrong, please restart game.")
            break
    return 0

hangman_words = [
"apple", "banana", "grape", "strawberry", "chocolate", "umbrella",
"rhinoceros", "xylophone", "juxtapose", "pneumonia", "quizzical", "kaleidoscope"
]
play_game(hangman_words)