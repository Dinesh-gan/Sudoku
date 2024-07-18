# SudokuGen.py

import random

def generate_sudoku():
    # Start with an empty Sudoku grid
    grid = [[0]*9 for _ in range(9)]
    
    # Fill the grid with a valid Sudoku puzzle
    fill_sudoku(grid)
    
    # Remove numbers to create a puzzle
    remove_numbers(grid)
    
    return grid

def fill_sudoku(grid):
    # Create a valid Sudoku puzzle by filling the grid with random numbers
    for row in range(9):
        for col in range(9):
            grid[row][col] = (row * 3 + row // 3 + col) % 9 + 1

def remove_numbers(grid, difficulty=0.5):
    # Remove numbers to create a puzzle based on difficulty level
    for row in range(9):
        for col in range(9):
            if random.random() < difficulty:
                grid[row][col] = 0
