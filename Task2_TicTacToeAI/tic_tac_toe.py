import random
# Tic Tac Toe Board

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

current_player = "X"
# Display Board
def display_board():

    print()

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")

    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")

    print(board[6] + " | " + board[7] + " | " + board[8])

    print()

# Check Winner
def check_winner():

    winning_combinations = [

        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:

        a, b, c = combo

        if board[a] == board[b] == board[c] != " ":
            return True

    return False
# Check Draw
def check_draw():

    return " " not in board
# Computer AI Move


    available_positions = []

    for i in range(9):

        if board[i] == " ":
            available_positions.append(i)

    move = random.choice(available_positions)

    board[move] = "O"
    # Smart AI Move
def ai_move():

    # First try winning move
    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            if check_winner():
                return

            board[i] = " "

    # Block player winning move
    for i in range(9):

        if board[i] == " ":

            board[i] = "X"

            if check_winner():

                board[i] = "O"
                return

            board[i] = " "

    # Otherwise random move
    available_positions = []

    for i in range(9):

        if board[i] == " ":
            available_positions.append(i)

    move = random.choice(available_positions)

    board[move] = "O"
# Main Game Loop
while True:

    display_board()

    position = int(input("Choose position (1-9): "))

    if board[position - 1] == " ":

        board[position - 1] = current_player

        # Check winner
        if check_winner():

            display_board()
            print(" Player Wins!")
            break

        # Check draw
        elif check_draw():

            display_board()
            print("It's a Draw!")
            break
                # AI Move
        ai_move()

        # Check AI Winner
        if check_winner():

            display_board()
            print(" Computer Wins!")
            break

        # Check Draw Again
        elif check_draw():

            display_board()
            print("It's a Draw!")
            break
            
    else:
        print("Position already taken!")
