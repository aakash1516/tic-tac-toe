import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Aakash Edition")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_widgets()
        self.moves_made = 0

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Player X's Turn", font=("Helvetica", 18), pady=10)
        self.label.pack()

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        for i in range(9):
            btn = tk.Button(self.frame, text="", font=("Helvetica", 24), width=5, height=2,
                            command=lambda i=i: self.on_button_click(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

        self.reset_button = tk.Button(self.root, text="Restart Game", font=("Helvetica", 14), command=self.reset_game)
        self.reset_button.pack(pady=10)

    def on_button_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            self.moves_made += 1

            winner = self.check_winner()
            if winner:
                self.label.config(text=f"Player {winner} Wins!")
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                return
            elif self.moves_made == 9:
                self.label.config(text="It's a Tie!")
                messagebox.showinfo("Game Over", "It's a Tie!")
                return

            self.current_player = "O" if self.current_player == "X" else "X"
            self.label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return self.board[a]
        return None

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.moves_made = 0
        for btn in self.buttons:
            btn.config(text="")
        self.label.config(text="Player X's Turn")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
