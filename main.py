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

def check(puzzle, number, position):
    """
    number - what we are checking
    position - where we are checking (y, x)
    boxes =
        0, 0 | 0, 1 | 0, 2
        -------------------
        1, 0 | 1, 1 | 1, 2
        -------------------
        2, 0 | 2, 1 | 2, 2
    """
    # row
    for item in range(len(puzzle[0])):
        if puzzle[position[0]][item] == number and position[1] != item:
            print("number already in row")
            return False
    # column
    for item in range(len(puzzle)):
        if puzzle[item][position[1]] == number and position[0] != item:
            print("number already in column")
            return False
    # square 
    box_y = position[0]//3
    box_x = position[1]//3
    #from index of box start eg box(0, 0) plus 3 for each item in box (0, 1), (0, 2), (0, 3), (1, 1), (1, 2)...(3, 3)
    for item_y in range(box_y*3, box_y*3 + 3):
        for item_x in range(box_x*3, box_x*3 + 3):
            if puzzle[item_y][item_x] == number and (item_y, item_x) != position:
                print("number already in box")
                return False


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

# print_puzzle(input)
# print(index_of_blank(input))
# check(input, 9, (0, 2))