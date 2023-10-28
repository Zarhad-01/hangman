import random as rand

# Task 1: Define list of possible words
word_list = ["apple", "banana", "plum", "dragonfruit", "durian"]
print(f"Task 1: word_list: {word_list}")

# Task 2: Choose a random word from the list
chosen_word = random.choice(word_list)
print(f"Task 2: chosen_word: {chosen_word}")

# Task 3: Ask user for an input
guess = input("Task 3: please input a letter to guess: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")