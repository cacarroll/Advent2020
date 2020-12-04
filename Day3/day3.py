# https://adventofcode.com/2020/day/3

with open("input.txt") as file:
    map = file.readlines()
    map = [line.strip() for line in map]

TreeCount = 0
row,col = 0,0

while row+1 < len(map):
    row += 1
    col += 3

    space = map[row][col % len(map[row])]
    if space == '#':
        TreeCount += 1

print(TreeCount)

# part 2
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

total = 1

for slope in slopes:
    TreeCount = 0
    row,col = 0,0

    while row+1 < len(map):
        col += slope[0]
        row += slope[1]

        space = map[row][col % len(map[row])]
        if space == '#':
            TreeCount += 1
    
    total *= TreeCount

print(total)
