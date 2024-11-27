import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_board(self):
        # Draw the grid
        for i in range(1, 3):
            self.canvas.create_line(0, i * 100, 300, i * 100, width=2)  # Horizontal lines
            self.canvas.create_line(i * 100, 0, i * 100, 300, width=2)  # Vertical lines

    def handle_click(self, event):
        # Determine the row and column clicked
        col = event.x // 100
        row = event.y // 100

        # Make a move if the cell is empty
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.draw_move(row, col)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                # Switch player
                self.current_player = "O" if self.current_player == "X" else "X"

    def draw_move(self, row, col):
        x0, y0 = col * 100, row * 100
        x1, y1 = x0 + 100, y0 + 100
        if self.current_player == "X":
            self.canvas.create_line(x0 + 10, y0 + 10, x1 - 10, y1 - 10, width=2, fill="blue")
            self.canvas.create_line(x0 + 10, y1 - 10, x1 - 10, y0 + 10, width=2, fill="blue")
        else:
            self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, width=2, outline="red")

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def is_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.canvas.delete("all")
        self.draw_board()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
