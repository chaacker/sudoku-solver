def print_solved(grid):
    for x in grid:
        for y in x:
            print(y, end=" ")
        print()

def row_check(grid, row, num):

    for j in range(9):
        if num == grid[row][j]:
            return False
    
    return True

def column_check(grid, col, num):

    for i in range(9):
        if num == grid[i][col]:
            return False
    
    return True

def subgrid_check(grid, row, col, num):

    r = (row // 3) * 3 + 1
    c = (col // 3) * 3 + 1

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if grid[r + i][c + j] == num:
                return False

    return True

def find_zeros(grid):

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j

    return -1, -1        

def solve(grid):

    i, j = find_zeros(grid)

    if i == -1 and j == -1:
        return True
    
    for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

        if row_check(grid, i, num) and column_check(grid, j, num) and subgrid_check(grid, i, j, num):

            grid[i][j] = num

            if solve(grid):
                return True
            
            grid[i][j] = 0
    
    return False

unsolved = [
    [0,0,5,9,0,0,0,0,1],
    [0,0,2,6,0,0,0,0,0],
    [0,0,4,0,0,3,0,5,2],
    [0,0,0,0,0,0,0,0,0],
    [0,0,1,0,4,0,0,0,7],
    [9,0,0,3,0,0,0,0,5],
    [8,0,0,7,0,0,0,0,3],
    [0,0,0,0,0,0,2,6,0],
    [1,0,0,0,0,6,7,0,0]
]

if solve(unsolved):
    print_solved(unsolved)
else:
    print("No solution!")
