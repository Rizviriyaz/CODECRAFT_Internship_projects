
# sudoku_solver.py
# Simple backtracking Sudoku solver
# Usage: python sudoku_solver.py puzzles/sample_puzzle.txt

import sys

def read_puzzle(path):
    with open(path) as f:
        lines = [line.strip() for line in f if line.strip()]
    grid = []
    for line in lines:
        # Accept digits and dots or zeros for empty
        row = []
        for ch in line.split():
            if ch in '.0' or ch == '0':
                row.append(0)
            else:
                row.append(int(ch))
        if len(row) == 9:
            grid.append(row)
    if len(grid) != 9:
        raise ValueError('Puzzle must have 9 rows of 9 values (space-separated).')
    return grid

def print_grid(grid):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print('-'*21)
        row = []
        for c in range(9):
            if c % 3 == 0 and c != 0:
                row.append('|')
            row.append(str(grid[r][c] or '.'))
        print(' '.join(row))

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def valid(grid, row, col, val):
    # Row
    if any(grid[row][c] == val for c in range(9)):
        return False
    # Column
    if any(grid[r][col] == val for r in range(9)):
        return False
    # Box
    box_r = (row // 3) * 3
    box_c = (col // 3) * 3
    for r in range(box_r, box_r+3):
        for c in range(box_c, box_c+3):
            if grid[r][c] == val:
                return False
    return True

def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    r, c = empty
    for val in range(1,10):
        if valid(grid, r, c, val):
            grid[r][c] = val
            if solve(grid):
                return True
            grid[r][c] = 0
    return False

def main():
    if len(sys.argv) < 2:
        print('Usage: python sudoku_solver.py path/to/puzzle.txt')
        return
    path = sys.argv[1]
    grid = read_puzzle(path)
    print('Input puzzle:')
    print_grid(grid)
    if solve(grid):
        print('\nSolved puzzle:')
        print_grid(grid)
    else:
        print('No solution found.')

if __name__ == '__main__':
    main()
