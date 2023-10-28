import random as rand
from milestone_4 import Hangman 

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print(f"You're out of lives!The word was {game.word}.")
            break
        elif '_' not in game.word_guessed:
            print(f"Congratulations! It was {game.word}, you guessed the word!")
            break
        elif game.num_lives > 0:
            game.ask_for_input()
        else:
            print("Something went wrong, please restart game.")
            break

hangman_words = [
"apple", "banana", "grape", "strawberry", "chocolate", "umbrella",
"rhinoceros", "xylophone", "juxtapose", "pneumonia", "quizzical", "kaleidoscope"
]
play_game(hangman_words)