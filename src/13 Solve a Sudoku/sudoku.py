''' Solve sudoku puzzle '''

def get_submatrix_3x3(puzzle, row, column):
    ''' Calculate and return a sudoku submatrix based
        on the position of the empty location.
    
    Indices of sudoku submatrices:

    # [0][0] -> [0][2]   [0][3] -> [0][5]   [0][6] -> [0][8]
    # [2][0] -> [2][2]   [2][3] -> [2][5]   [2][6] -> [2][8]

    # [3][0] -> [3][2]   [3][3] -> [3][5]   [3][6] -> [3][8]
    # [5][0] -> [5][2]   [5][3] -> [5][5]   [5][6] -> [5][8]

    # [6][0] -> [6][2]   [6][3] -> [6][5]   [6][6] -> [6][8]
    # [8][0] -> [8][2]   [8][3] -> [8][5]   [8][6] -> [8][8]
    '''
    if row in range(0, 3):
        start_row = 0
        end_row = 3
    elif row in range(3, 6):
        start_row = 3
        end_row = 6
    elif row in range (6, 9):
        start_row = 6
        end_row = 9

    if column in range(0, 3):
        start_col = 0
        end_col = 3
    elif column in range(3, 6):
        start_col = 3
        end_col = 6
    elif column in range (6, 9):
        start_col = 6
        end_col = 9

    submatrix = [row[start_col:end_col] for row in puzzle[start_row:end_row]]
    return submatrix

def find_empty_location(puzzle):
    ''' Find the location with 0 '''
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None

def solve_sudoku(puzzle):
    ''' Solve sudoku puzzle '''
    # Find an empty location
    empty_location = find_empty_location(puzzle)

    if not empty_location:
        return True

    row, col = empty_location

    # calculate to corresponding submatrix
    submatrix_3x3 = get_submatrix_3x3(puzzle, row, col)

    # try one number
    for number in range(1,10):
        # check that the number is not already in the row i,
        # in the column j and in the submatrix
        if ((number not in puzzle[row]) and
            all(r[col] != number for r in puzzle) and
            (number not in submatrix_3x3)):

            # set new number
            puzzle[row][col] = number
            
            if solve_sudoku(puzzle):
                return True
            
            # Revert the newly set number back to 0 i case the number 
            # is not leading to the solution
            puzzle[row][col] = 0
    
    # When it is not possible to set a number backtrack
    return False

if __name__ == '__main__':
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    solve_sudoku(puzzle)

    for row in puzzle:
        print(row)
