input = [
    [8, 2, 0, 0, 0, 1, 0, 3, 6],
    [3, 0, 0, 8, 6, 0, 9, 0, 0],
    [0, 5, 0, 9, 0, 0, 7, 0, 4],
    [0, 0, 0, 2, 9, 7, 6, 5, 3],
    [7, 0, 5, 0, 8, 0, 2, 0, 1],
    [6, 3, 2, 0, 5, 4, 0, 0, 0],
    [5, 0, 4, 0, 0, 2, 0, 9, 0],
    [0, 0, 1, 0, 4, 8, 0, 0, 7],
    [2, 8, 0, 7, 0, 0, 0, 6, 5]
]

valid = [
    [8, 2, 9, 4, 7, 1, 5, 3, 6],
    [3, 4, 7, 8, 6, 5, 9, 1, 2],
    [1, 5, 6, 9, 2, 3, 7, 8, 4],
    [4, 1, 8, 2, 9, 7, 6, 5, 3],
    [7, 9, 5, 3, 8, 6, 2, 4, 1],
    [6, 3, 2, 1, 5, 4, 8, 7, 9],
    [5, 7, 4, 6, 3, 2, 1, 9, 8],
    [9, 6, 1, 5, 4, 8, 3, 2, 7],
    [2, 8, 3, 7, 1, 9, 4, 6, 5]
]

def print_puzzle(puzzle):
    for row in range(len(puzzle)):
        # creating 3x3 boxes
        if row % 3 == 0 and row != 0:
            print("-----------------------")
        for column in range(len(puzzle[0])):
            if column % 3 == 0 and column != 0:
                print(" | ", end = "")
            
            # final item in row
            if column == 8:
                print(puzzle[row][column])
            # print each num
            else:
                print(str(puzzle[row][column]) + " ", end = "")

def index_of_blank(puzzle):
    """
    When working with 2D arrays in programming, the standard is to represent the location 
        of an element using (row, column) or (y, x). The first value typically represents 
        the vertical position (row/y), and the second value represents the horizontal 
        position (column/x).
    """
    for row in range(len(puzzle)):
        # for each item in the row
        for column in range(len(puzzle[0])):
            if puzzle[row][column] == 0:
                return (row, column)
    return

print_puzzle(input)
print(index_of_blank(input))
