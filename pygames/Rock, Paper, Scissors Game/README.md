# Rock, Paper, Scissors Game

Welcome to the Rock, Paper, Scissors game! This is a simple console-based game where you can challenge the computer in a classic game of chance.

## Table of Contents

- [Game Overview](#game-overview)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [Game Logic](#game-logic)
- [Example Output](#example-output)


## Game Overview

In this game, you will choose one of three options: Rock, Paper, or Scissors. The computer will also make a random choice, and the winner will be determined based on the rules of the game:

- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock

## How to Play

1. Choose your move by typing "rock", "paper", or "scissors".
2. The computer will randomly select its move.
3. The winner will be announced based on the choices made.
4. To exit the game, type "exit".

## Installation

To run this game, you need to have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

Clone this repository or download the `rock_paper_scissors.py` file:

1. Clone the repository.
```
git clone https://github.com/yourusername/rock-paper-scissors.git
```
2. Navigate to the `rock_paper_scissors` folder.
```
cd rock-paper-scissors
```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the game:
   ```
   python main.py
   ```
## Game Logic
The game is implemented using simple conditionals to determine the winner based on player and computer choices. The choices are validated to ensure they are one of the valid options.

## Example Output
```
Welcome to Rock, Paper, Scissors!
Enter rock, paper, or scissors (or 'exit' to quit): rock
Computer chose: scissors
You win!

Enter rock, paper, or scissors (or 'exit' to quit): paper
Computer chose: rock
You win!

Enter rock, paper, or scissors (or 'exit' to quit): scissors
Computer chose: paper
You win!

Enter rock, paper, or scissors (or 'exit' to quit): exit
Thanks for playing!
```

