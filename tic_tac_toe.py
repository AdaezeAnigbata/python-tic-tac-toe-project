
from random import randrange


PLAYER = "O"
COMPUTER = "X"

# Each winning line is stored as three board positions.
WINNING_LINES = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0))
)

scores = {"You": 0, "Computer": 0, "Ties": 0}

current_streaks = {"You": 0, "Computer": 0}
best_streaks = {"You": 0, "Computer": 0}


# Create a fresh board for each round.
def new_board():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


# Display the board and highlight a winning line when one exists.
def display_board(board, winning_line=None):
    print("+-------+-------+-------+")

    for row in range(3):
        print("|       |       |       |")
        print("|", end="")

        for column in range(3):
            square = board[row][column]

            if winning_line and (row, column) in winning_line:
                cell = f"  *{square}*  "
            else:
                cell = f"   {square}   "

            print(cell + "|", end="")

        print()
        print("|       |       |       |")
        print("+-------+-------+-------+")


# Ask the player to choose an available square.
def enter_move(board):
    while True:
        try:
            move = int(input("Choose a square (1-9): "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if move < 1 or move > 9:
            print("Choose a number between 1 and 9.")
            continue

        row = (move - 1) // 3
        column = (move - 1) % 3

        if board[row][column] in (PLAYER, COMPUTER):
            print("That square is already taken.")
            continue

        board[row][column] = PLAYER
        return


# Return the coordinates of every available square.
def free_squares(board):
    free = []

    for row in range(3):
        for column in range(3):
            if board[row][column] not in (PLAYER, COMPUTER):
                free.append((row, column))

    return free


# Find a winning line for the specified player.
def winning_combination(board, sign):
    for line in WINNING_LINES:
        if all(board[row][column] == sign for row, column in line):
            return line

    return None


# Check whether a player has won.
def victory_for(board, sign):
    return winning_combination(board, sign) is not None


# Find a move that would give the specified player a win.
def find_winning_move(board, sign):
    for row, column in free_squares(board):
        original_value = board[row][column]
        board[row][column] = sign

        if victory_for(board, sign):
            board[row][column] = original_value
            return row, column

        board[row][column] = original_value

    return None


# Let the computer win if possible, block the player, or choose randomly.
def draw_move(board):
    move = find_winning_move(board, COMPUTER)

    if move is None:
        move = find_winning_move(board, PLAYER)

    if move is None:
        free = free_squares(board)
        move = free[randrange(len(free))]

    row, column = move
    board[row][column] = COMPUTER


# Determine whether the round has ended.
def game_result(board):
    if victory_for(board, PLAYER):
        return "You"

    if victory_for(board, COMPUTER):
        return "Computer"

    if not free_squares(board):
        return "Tie"

    return None


# Update the current and highest winning streaks.
def update_streaks(result):
    # A tie leaves both streaks unchanged.
    if result == "Tie":
        return

    for name in ("You", "Computer"):
        if name == result:
            current_streaks[name] += 1

            if current_streaks[name] > best_streaks[name]:
                best_streaks[name] = current_streaks[name]
        else:
            current_streaks[name] = 0


# Play one round.
def play_round(starting_player):
    board = new_board()
    current_player = starting_player

    # The computer starts in the centre when it starts a round.
    if starting_player == COMPUTER:
        board[1][1] = COMPUTER
        current_player = PLAYER

    print("\nNew round!")
    display_board(board)

    while True:
        if current_player == PLAYER:
            enter_move(board)
        else:
            print("Computer's move...")
            draw_move(board)

        result = game_result(board)

        if result is not None:
            winning_line = None

            if result == "You":
                winning_line = winning_combination(board, PLAYER)
            elif result == "Computer":
                winning_line = winning_combination(board, COMPUTER)

            display_board(board, winning_line)
            return result

        display_board(board)

        current_player = (
            COMPUTER if current_player == PLAYER else PLAYER
        )


# Display scores and streak statistics.
def show_scores(rounds_played):
    print("\n----- Score Summary -----")
    print("Your wins:", scores["You"])
    print("Computer wins:", scores["Computer"])
    print("Ties:", scores["Ties"])
    print("Rounds played:", rounds_played)

    if rounds_played > 0:
        percentage = scores["You"] / rounds_played * 100
        print("Your win percentage:", round(percentage, 1), "%")

    print("\n----- Winning Streaks -----")
    print("Your current streak:", current_streaks["You"])
    print("Computer's current streak:", current_streaks["Computer"])
    print("Your best streak:", best_streaks["You"])
    print("Computer's best streak:", best_streaks["Computer"])
    print("---------------------------")


# Run the game.
def main():
    rounds_played = 0
    starting_player = COMPUTER

    print("Welcome to Tic-Tac-Toe!")
    print("You are O. The computer is X.")
    print("The computer starts the first round in the centre.")

    while True:
        result = play_round(starting_player)
        rounds_played += 1

        if result == "You":
            print("You won!")
            scores["You"] += 1
            starting_player = PLAYER

        elif result == "Computer":
            print("The computer won!")
            scores["Computer"] += 1
            starting_player = COMPUTER

        else:
            print("It's a tie!")
            scores["Ties"] += 1

            # Switch the starting player, but keep both streaks.
            starting_player = (
                PLAYER if starting_player == COMPUTER else COMPUTER
            )

        update_streaks(result)
        show_scores(rounds_played)

        while True:
            answer = input("\nPlay again? (y/n): ").strip().lower()

            if answer in ("y", "n"):
                break

            print("Please enter y or n.")

        if answer == "n":
            break

        if starting_player == COMPUTER:
            print("The computer will start the next round.")
        else:
            print("You will start the next round.")

    print("\nThanks for playing!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame closed.")
