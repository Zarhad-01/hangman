# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description

The aim of this project is to provide a digital version of the traditional Hangman game. This implementation provides a platform for users to play against the computer. Throughout the development of this project, I learned about handling user input, implementing game logic, and creating an interactive command-line interface.

## Installation

1. Clone the repository to your local machine using `git clone <repository-link>`.
2. Navigate to the directory containing the game using `cd hangman`.
3. Ensure you have Python installed on your system. If not, download it from [Python's official website](https://www.python.org/).

## Usage

1. Run the game by executing `python milestone_[1, 2, 3, 4, or 5].py` in the command line.
2. Follow the on-screen instructions to play the game. You will be prompted to guess letters until you either guess the word or run out of attempts.
## Milestones

### Milestone 2 - Basic Word Guessing (`milestone_2.py`)

In this milestone:

- A list of possible words is defined.
- A random word is selected from the list.
- The user is prompted to input a letter to guess. 

### Milestone 3 - Enhanced Input Verification (`milestone_3.py`)

In this milestone:

- The program iteratively checks if the user's input is a valid guess.
- The guessed letter is checked against the selected word.
- Functions are introduced to streamline the checking process and obtain user input.

### Milestone 4 - Object-Oriented Hangman (`milestone_4.py`)

In this milestone:

- The Hangman game is structured as an object-oriented class.
- The `Hangman` class handles the game's state and provides methods for checking guesses and obtaining user input.
- The number of lives the player has is tracked, and feedback is provided to the user as they guess letters.
- If the player runs out of lives or successfully guesses the word, appropriate end-of-game messages are displayed.

### Milestone 5 - Game Loop Integration (`milestone_5.py`)

In this milestone:

- The previous `Hangman` class from Milestone 4 is imported and utilized.
- A game loop is implemented to continuously prompt the user for input until the game concludes.
- The game's ending conditions are clearly defined, whether the player runs out of lives, successfully guesses the word, or an unexpected error occurs.
- This milestone streamlines the game-playing experience by integrating the core functionalities into a cohesive loop.

## File Structure
```
hangman/
│   .gitignore
│   README.md
│
└───hangman/
        hangman_Template.py
        milestone_2.py
hangman/
│   .gitignore
│   README.md
│
└───hangman/
        hangman_Template.py
        milestone_2.py
        milestone_3.py
hangman/
│   .gitignore
│   README.md
│
└───hangman/
        hangman_Template.py
        milestone_2.py
        milestone_3.py
        milestone_4.py
        milestone_5.py
```
## License

This project is open source and available under the [MIT License](LICENSE).
