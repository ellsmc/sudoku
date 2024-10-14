puzzle = []
with open("puzzle_easy.txt") as puzzle_text:
    for line in puzzle_text:
        #puzzle.append(line.strip())
        puzzle.append([int(x) for x in line.split(', ')])

print(puzzle)

puz2 = [
    [7, 4, 5, 3, 9, 6, 0, 2, 8],
    [0, 9, 0, 0, 8, 4, 0, 7, 3],
    [8, 0, 2, 1, 0, 0, 0, 4, 0],
    [0, 0, 1, 9, 2, 0, 0, 0, 0],
    [0, 0, 9, 0, 0, 3, 0, 1, 5],
    [0, 0, 0, 0, 0, 0, 6, 9, 2],
    [0, 0, 0, 6, 0, 2, 3, 0, 0],
    [0, 5, 7, 0, 0, 1, 4, 6, 0],
    [0, 1, 3, 0, 0, 0, 0, 0, 7],
]
print(puz2)