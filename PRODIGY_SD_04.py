def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def find_empty_location(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_safe(grid, row, col, num):
    # Check if 'num' is not in current row
    if num in grid[row]:
        return False
    
    # Check if 'num' is not in current column
    if num in [grid[i][col] for i in range(9)]:
        return False
    
    # Check if 'num' is not in current 3x3 box
    box_row_start = row - row % 3
    box_col_start = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[box_row_start + i][box_col_start + j] == num:
                return False
    
    return True

def solve_sudoku(grid):
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True  # Puzzle solved
    
    row, col = empty_location
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Reset if backtrack
    
    return False

def get_user_input():
    grid = []
    print("Enter the Sudoku puzzle row by row. Use 0 for empty cells:")
    for _ in range(9):
        while True:
            try:
                row = list(map(int, input().split()))
                if len(row) == 9 and all(0 <= num <= 9 for num in row):
                    grid.append(row)
                    break
                else:
                    print("Invalid input. Please enter 9 numbers between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter 9 numbers between 0 and 9.")
    return grid

if __name__ == "__main__":
    sudoku_grid = get_user_input()

    print("\nUnsolved Sudoku puzzle:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku puzzle:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists.")
