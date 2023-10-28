import random as rand

class Hangman:
    """
    Represent the Hangman game.

    Attributes:
        word (str): The secret word to be guessed.
        word_guessed (list): The current representation of the word with underscores for unguessed letters.
        num_lives (int): The remaining number of incorrect guesses allowed.
        list_of_guesses (list): The letters guessed so far.
    """

    def __init__(self, word_list, num_lives=5):
        self.word = rand.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Check the player's guess against the secret word.

        Parameters:
            guess (str): The letter guessed by the player.
        """
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = guess
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Prompt the player for a guess and update the game state accordingly.
        """
        while self.num_lives > 0 and '_' in self.word_guessed:
            print("Current word:", ' '.join(self.word_guessed))
            guess = input("Please input a letter: ")

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You already tried {guess}! Previous guesses: {' '.join(self.list_of_guesses)}")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

if __name__ == "__main__":
    hangman_words = [
    "apple", "banana", "grape", "strawberry", "chocolate", "umbrella",
    "rhinoceros", "xylophone", "juxtapose", "pneumonia", "quizzical", "kaleidoscope"
    ]

    hm = Hangman(hangman_words)
    hm.ask_for_input()