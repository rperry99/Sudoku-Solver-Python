# Sudoku Solver
Using:
- Recursion
- Backtracking

---
To Run: 
- `python3 Sudoku_Solver.py`

---
Notes:
- Inspired from [Kylie Ying](https://github.com/kying18)'s YouTube video found [here](https://www.youtube.com/watch?v=tvP_FZ-D9Ng).
- This implemented recursion so that the program will keep calling the function `solve_puzzle()` until the puzzle is solved.
- Sudoku_Solver takes advantage of mutable data as well. Every time the puzzle gets updated, the functions then use this updated puzzle to continue working.
- How does this work?
    - This will first check to find the first empty square within the puzzle. (Empty squares are represented with a `-1`.)
    - Then once it has this empty square, the program will go through the numbers from 1-9 until it detects that there is a valid entry.
        - The program will check to see if the number being tested is already in the row.
        - Then check if it's already in the column.
        - Then check if it's already in the 3x3 grid that it's in.
    - If all of these checks are good, it moves on to the next square.
    - This continues until the puzzle is finished.
    - If the program cannot place a 1-9 in a square, `solve_puzzle()` will return `None`, and thus will end the program and show that the puzzle is not solvable.

---
Function Explanations:
- `solve_puzzle(puzzle)`
    - Takes in a puzzle, and this is where the main functionality of this program lies.
    - It calls the below two functions to find the next empty square, and to try different number options within that square.
    - When it finds a correct answer, then it assigns it to the cell.
- `find_next_empty(puzzle)`
    - Also takes in a puzzle. 
    - The sole purpose of this helper function is to find the next empty square within the grid.
- `is_valid(puzzle, guess, row, col)`
    - Takes:
        - A puzzle to work on.
        - The current guess. For example, if the program is trying the number 3 in the current square.
        - The row and column that is currently being checked.
    - Returns true if the guess can legally be placed in the cell