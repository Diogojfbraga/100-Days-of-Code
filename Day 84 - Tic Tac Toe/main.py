## Tic Tac Toe Board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


## Tic Tac Toe Positions
## Each position links to its row and column on the board
positions = {
    "A1": [0, 0],
    "A2": [0, 1],
    "A3": [0, 2],
    "B1": [1, 0],
    "B2": [1, 1],
    "B3": [1, 2],
    "C1": [2, 0],
    "C2": [2, 1],
    "C3": [2, 2]
}

## Store the positions played by X and O
plays = {}


## Display the board
def print_board(board):
    print("\n    1   2   3")

    for i, row in enumerate(board):
        print(f"{'ABC'[i]}   {' | '.join(row)}")

        if i < 2:
            print("   ---+---+---")


## Player One - X
def player_one():
    player_one = input("What is your play? (Letter+Number, Ex.A2) You are 'X' ").upper()

    ## Check if the position exists and has not been played
    if player_one not in plays and player_one in positions:
        for position in positions:
            if player_one == position and position not in plays:
                board_position = positions[player_one]

                ## Update the board and save the move
                board[board_position[0]][board_position[1]] = 'X'
                plays[player_one] = "X"

    elif player_one in plays:
        print("Position already taken")
    else:
        print("Position does not exist")


## Player Two - O
def player_two():
    player_two = input("What is your play? (Letter+Number, Ex.A2) You are 'O' ").upper()

    ## Check if the position exists and has not been played
    if player_two not in plays and player_two in positions:
        for position in positions:
            if player_two == position and position not in plays:
                board_position = positions[position]

                ## Update the board and save the move
                board[board_position[0]][board_position[1]] = 'O'
                plays[player_two] = "O"

    elif player_two in plays:
        print("Position already taken")
    else:
        print("Position does not exist")


## Main game loop - maximum of 9 moves
while len(plays) < 9:

    ## Check if Player X has completed a row, column or diagonal
    if (
        # Rows
        (plays.get('A1') == 'X' and plays.get('A2') == 'X' and plays.get('A3') == 'X') or
        (plays.get('B1') == 'X' and plays.get('B2') == 'X' and plays.get('B3') == 'X') or
        (plays.get('C1') == 'X' and plays.get('C2') == 'X' and plays.get('C3') == 'X') or

        # Columns
        (plays.get('A1') == 'X' and plays.get('B1') == 'X' and plays.get('C1') == 'X') or
        (plays.get('A2') == 'X' and plays.get('B2') == 'X' and plays.get('C2') == 'X') or
        (plays.get('A3') == 'X' and plays.get('B3') == 'X' and plays.get('C3') == 'X') or

        # Diagonals
        (plays.get('A1') == 'X' and plays.get('B2') == 'X' and plays.get('C3') == 'X') or
        (plays.get('A3') == 'X' and plays.get('B2') == 'X' and plays.get('C1') == 'X')
    ):
        print("Player X Wins!")
        print("GAME OVER")
        break

    ## Display board and ask Player X for a move
    print_board(board)
    player_one()

    ## Check if Player O has completed a row, column or diagonal
    if (
        # Rows
        (plays.get('A1') == 'O' and plays.get('A2') == 'O' and plays.get('A3') == 'O') or
        (plays.get('B1') == 'O' and plays.get('B2') == 'O' and plays.get('B3') == 'O') or
        (plays.get('C1') == 'O' and plays.get('C2') == 'O' and plays.get('C3') == 'O') or

        # Columns
        (plays.get('A1') == 'O' and plays.get('B1') == 'O' and plays.get('C1') == 'O') or
        (plays.get('A2') == 'O' and plays.get('B2') == 'O' and plays.get('C2') == 'O') or
        (plays.get('A3') == 'O' and plays.get('B3') == 'O' and plays.get('C3') == 'O') or

        # Diagonals
        (plays.get('A1') == 'O' and plays.get('B2') == 'O' and plays.get('C3') == 'O') or
        (plays.get('A3') == 'O' and plays.get('B2') == 'O' and plays.get('C1') == 'O')
    ):
        print("Player O Wins!")
        print("GAME OVER")
        break

    ## Display board and ask Player O for a move
    print_board(board)
    player_two()