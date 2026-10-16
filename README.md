# Tic-Tac-Toe with Python

A command-line Tic-Tac-Toe game where you play as **O** against a computer opponent marked **X**.

I built this project to practice bringing Python fundamentals together in a complete, playable application. Beyond the usual turn-based gameplay, the computer can take a winning move or block an immediate threat, while the game keeps track of scores and winning streaks across rounds.

## Features

- **Interactive gameplay:** Choose a square by entering a number from 1 to 9.
- **Computer opponent:** The computer looks for an immediate win first, blocks a possible player win when necessary, and otherwise selects a random available square.
- **Winning-line display:** The three squares that complete a winning combination are highlighted at the end of a round.
- **Score tracking:** View the number of wins for each side, ties, total rounds played, and your win percentage.
- **Winning streaks:** Track current and highest winning streaks for both players. A tie leaves existing streaks unchanged.
- **Changing starting player:** The computer starts the first round. After a win, the winner starts the next round; after a tie, the starting player switches.
- **Input validation:** Invalid numbers, non-numeric entries, and occupied squares are handled without ending the game.
- **Clean exit:** The game handles Ctrl+C and Ctrl+D without displaying a Python traceback.

## Requirements

- Python 3
- A terminal or command-line interface

No third-party packages are required.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AdaezeAnigbata/python-tic-tac-toe-project.git
```

### 2. Enter the project directory

```bash
cd python-tic-tac-toe
```

### 3. Run the game

```bash
python tic_tac_toe.py
```

If your system uses `python3` instead, run:

```bash
python3 tic_tac_toe.py
```

## How to Play

1. The board contains nine numbered squares.
2. You play as **O**, and the computer plays as **X**.
3. Enter the number of the square where you want to place your mark.
4. The computer makes its move automatically.
5. The round ends when either side gets three marks in a row, column, or diagonal, or when the board is full.
6. Review the score summary and choose whether to play another round.

The computer follows a simple strategy rather than choosing every move randomly. It prioritizes an immediate win, then blocks an immediate threat. It does not plan several moves ahead, so it can still make mistakes.

## Python Concepts Practiced

Building the game gave me an opportunity to apply several concepts in one project:

- **Functions:** Separating tasks such as displaying the board, validating moves, checking winners, and updating scores.
- **Lists and nested lists:** Representing the board and accessing individual squares using row and column positions.
- **Loops and conditionals:** Managing turns, checking available moves, and controlling the game flow.
- **Input validation and exception handling:** Handling invalid entries and unexpected interruptions.
- **Random selection:** Choosing an available square when the computer has no immediate win or block.
- **Constants:** Keeping player symbols and winning combinations in one place.
- **State management:** Tracking scores and winning streaks across multiple rounds.
- **Testing and debugging:** Checking different game outcomes, starting-player scenarios, and invalid input.

## Project Structure

```text
python-tic-tac-toe/
├── tic_tac_toe.py
├── README.md
└── .gitignore
```

## Possible Improvements

There is room to extend the project as I continue learning Python. Some ideas include saving scores between sessions, adding difficulty levels, and improving the computer's strategy to consider future moves.

## Project Status

The project is playable and includes a basic computer strategy, score tracking, winning-streak statistics, and winning-line highlighting. It is a learning project that I plan to improve as I develop my Python skills.
