# main.py

import tkinter as tk
from tkinter import messagebox
from SudokuGen import generate_sudoku
from HintGenerator import generate_hint  # Import the hint generator function

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game")
        self.board = [[0]*9 for _ in range(9)]
        self.selected = None
        self.hinted_cell = None  # To store the rectangle ID for the hinted cell
        self.create_widgets()
        self.draw_board()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=450, height=450)
        self.canvas.pack()

        self.draw_grid()
        self.canvas.bind("<Button-1>", self.cell_clicked)  # Bind left-click event
        self.canvas.bind("<Double-Button-1>", self.cell_double_clicked)  # Bind double-click event
        self.root.bind("<KeyPress>", self.key_pressed)

        self.generate_button = tk.Button(self.root, text="Generate", command=self.generate_sudoku)
        self.generate_button.pack()

    def draw_grid(self):
        for i in range(10):
            color = "black" if i % 3 == 0 else "gray"
            self.canvas.create_line(50 * i, 0, 50 * i, 450, fill=color)
            self.canvas.create_line(0, 50 * i, 450, 50 * i, fill=color)

    def draw_board(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                num = self.board[i][j]
                if num != 0:
                    x = j * 50 + 25
                    y = i * 50 + 25
                    self.canvas.create_text(x, y, text=num, tags="numbers", font=("Arial", 20))

    def cell_clicked(self, event):
        if self.selected:
            self.canvas.delete(self.selected)
        x, y = event.x // 50, event.y // 50
        self.selected = self.canvas.create_rectangle(
            x * 50, y * 50, (x + 1) * 50, (y + 1) * 50,
            outline="blue", width=2
        )

    def cell_double_clicked(self, event):
        x, y = event.x // 50, event.y // 50
        if self.board[y][x] == 0:  # Only provide hint for empty cells
            hint = generate_hint(self.board)
            if hint:
                row, col, answer = hint
                self.board[row][col] = answer
                self.canvas.delete(self.hinted_cell)  # Delete previously hinted cell if any
                x1, y1 = col * 50, row * 50
                x2, y2 = (col + 1) * 50, (row + 1) * 50
                self.hinted_cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="blue", width=2)
                self.draw_board()
            else:
                messagebox.showinfo("No Hint", "No empty cell found to provide a hint.")

    def key_pressed(self, event):
        if self.selected:
            x1, y1, x2, y2 = map(int, self.canvas.coords(self.selected))  # Convert coordinates to integers
            cell_x, cell_y = x1 // 50, y1 // 50  # Calculate cell indices
            if event.char.isdigit() and 1 <= int(event.char) <= 9:
                self.board[cell_y][cell_x] = int(event.char)
                self.draw_board()
            elif event.keysym in ["Left", "Right", "Up", "Down"]:
                new_x = cell_x
                new_y = cell_y
                if event.keysym == "Left" and cell_x > 0:
                    new_x = cell_x - 1
                elif event.keysym == "Right" and cell_x < 8:
                    new_x = cell_x + 1
                elif event.keysym == "Up" and cell_y > 0:
                    new_y = cell_y - 1
                elif event.keysym == "Down" and cell_y < 8:
                    new_y = cell_y + 1
                self.canvas.delete(self.selected)
                self.selected = self.canvas.create_rectangle(
                    new_x * 50, new_y * 50, (new_x + 1) * 50, (new_y + 1) * 50,
                    outline="blue", width=2
                )

    def generate_sudoku(self):
        self.board = generate_sudoku()
        self.draw_board()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    game.run()
