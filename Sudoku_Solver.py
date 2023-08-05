# Helper Function to find the empty spaces
def find_next_empty(puzzle):
    # Finds the next row / column on the puzzle that has not yet been filled.
    # Empty spaces are represented with a -1.

    # Iterate through the rows and columns until the computer finds a -1.
    # When it does, return that row, column.
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return row, column
    
    # Once all the spaces are filled, we return none, none
    return None, None

# Helper function to see if the guess is a valid one. If there are no conflicts, it is considered valid. If there are, it's invalid.
def is_valid(puzzle, guess, row, col):

    # Check the row:
    row_values = puzzle[row]
    if guess in row_values:
        return False

    # Check the columns:
    col_values = []
    for i in range(9):
        col_values.append(puzzle[i][col])
    if guess in col_values:
        return False
    
    # Check the 3x3 matrix:
    # Find where the 3x3 starts, then iterate from there.
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    # Iterate over the 3x3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    # If it didn't find a duplicate number anywhere, then this is now valid.
    return True

# Function that solves the puzzle
def solve_puzzle(puzzle):
    # Solving Sudoku using a backtracking technique
    # I'm passing in a list of lists, that represents the puzzle.
    # I then return if there is a solution that exists. If the solution DOES exist, then I will return the solved puzzle.

    # Choose somewhere on the puzzle to begin.
    row, col = find_next_empty(puzzle)

    # Once puzzle is filled, it's complete. I did not allow for incorrect answers to be entered.
    if row == None:
        return True

    # In the blank space, I want the computer to make a guess (1-9). 
    for guess in range(1, 10):

        # Check for valid guess.
        if is_valid(puzzle, guess, row, col):
            # Place the valid guess in the correct spot in the puzzle.
            puzzle[row][col] = guess

            # Guess the next number
            if solve_puzzle(puzzle):
                return True;
            
        # Backtrack if something is not valid or an answer is incorrect
        puzzle[row][col] = -1 # make the grid space blank again.

    # If all possible numbers (1-9) are not valid, then the puzzle is unsolvable. 
    return False;

<<<<<<< HEAD
# Run Sudoku_Solver.py
=======
>>>>>>> 69c57dc7ae92978e661fc79884c95dd7d7654503
if __name__ == '__main__':
    example_board = [
        [3, 9, 1,  -1, 5, -1,  -1, -1, -1],
        [-1, -1, -1,  2, -1, -1,  -1, -1, 5],
        [-1, -1, -1,  7, 1, 9,  -1, 8, -1],

        [-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
        [2, -1, 6,  -1, -1, 3,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],

        [5, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [6, 7, -1,  1, -1, 5,  -1, 4, -1],
        [1, -1, 9,  -1, -1, -1,  2, -1, -1]
    ]
    print(solve_puzzle(example_board))
    print(example_board)