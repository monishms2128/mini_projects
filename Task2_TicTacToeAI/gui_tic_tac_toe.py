import tkinter as tk
import random
from tkinter import messagebox

# Main Window
window = tk.Tk()
window.title("Tic Tac Toe AI")
window.geometry("500x650")
window.configure(bg="#1e1e1e")

# Board
board = [" " for _ in range(9)]

buttons = []

# Scores
player_score = 0
computer_score = 0
draw_score = 0

# Score Label
score_label = tk.Label(
    window,
    text="Player: 0   Computer: 0   Draws: 0",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white"
)

score_label.grid(row=3, column=0, columnspan=3, pady=10)


# Check Winner
def check_winner(player):

    win_positions = [

        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in win_positions:

        a, b, c = combo

        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Check Draw
def check_draw():

    return " " not in board


# Reset Game
def reset_game():

    global board

    board = [" " for _ in range(9)]

    for button in buttons:

        button.config(text=" ", state="normal")


# AI Move
def ai_move():

    global computer_score
    global draw_score

    available = []

    for i in range(9):

        if board[i] == " ":
            available.append(i)

    if available:

        move = random.choice(available)

        board[move] = "O"

        buttons[move].config(text="O", state="disabled")

        # Computer Wins
        if check_winner("O"):

            computer_score += 1

            score_label.config(
                text=f"Player: {player_score}   Computer: {computer_score}   Draws: {draw_score}"
            )

            messagebox.showinfo("Game Over", "🤖 Computer Wins!")

            reset_game()

        # Draw
        elif check_draw():

            draw_score += 1

            score_label.config(
                text=f"Player: {player_score}   Computer: {computer_score}   Draws: {draw_score}"
            )

            messagebox.showinfo("Game Over", "It's a Draw!")

            reset_game()


# Player Move
def player_move(index):

    global player_score
    global draw_score

    if board[index] == " ":

        board[index] = "X"

        buttons[index].config(text="X", state="disabled")

        # Player Wins
        if check_winner("X"):

            player_score += 1

            score_label.config(
                text=f"Player: {player_score}   Computer: {computer_score}   Draws: {draw_score}"
            )

            messagebox.showinfo("Game Over", "🎉 You Win!")

            reset_game()

        # Draw
        elif check_draw():

            draw_score += 1

            score_label.config(
                text=f"Player: {player_score}   Computer: {computer_score}   Draws: {draw_score}"
            )

            messagebox.showinfo("Game Over", "It's a Draw!")

            reset_game()

        else:
            ai_move()


# Create Buttons
for i in range(9):

    button = tk.Button(
        window,
        text=" ",
        font=("Arial", 28, "bold"),
        width=6,
        height=3,
        bg="#2d2d2d",
        fg="white",
        activebackground="#007acc",
        activeforeground="white",
        command=lambda i=i: player_move(i)
    )

    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)

    buttons.append(button)


# Restart Button
restart_button = tk.Button(
    window,
    text="Restart Game",
    font=("Arial", 16, "bold"),
    bg="#007acc",
    fg="white",
    command=reset_game
)

restart_button.grid(row=4, column=0, columnspan=3, pady=20)

# Run Window
window.mainloop()