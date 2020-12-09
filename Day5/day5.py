def getNewRange(letter, lowerRange, upperRange):
    if letter == 'F' or letter == 'L':
        #Keep lower half in range
        middle = int((upperRange - lowerRange) / 2) + lowerRange
        newRange = lowerRange, middle
        return newRange

    if letter == 'B' or letter == 'R':
        # Keep upper half
        middle = int((upperRange - lowerRange) / 2 ) + lowerRange +1
        newRange = middle, upperRange
        return newRange
    
seats = []
with open('Day5\\input.txt') as file:
    lines = [str(line.rstrip()) for line in file]
    for line in lines:
        value = line
        rows = value[0:10]
        count = 1
        lowerRange, upperRange = int(0), int(127)
        for letter in rows:
            result = getNewRange(letter, lowerRange, upperRange)
            lowerRange = result[0]
            upperRange = result[1]
            if count == 7 and letter == 'F':
                row = lowerRange
                lowerRange = int(0)
                upperRange = int(7)
            if count == 7 and letter == 'B':
                row = upperRange
                lowerRange = int(0)
                upperRange = int(7)
            if count == 10 and letter == 'R':
                column = upperRange
            if count == 10 and letter == 'L':
                column = lowerRange
            count +=1
        seat = (row * 8 + column)
seats.append(seat)
print(max(seats))

# print (getNewRange('F', 0, 127))
assert getNewRange('F', 0, 127) == (0, 63)
assert getNewRange('B', 0, 63) == (32, 63)
assert getNewRange('F', 32, 63) == (32, 47)
assert getNewRange('B', 32, 47) == (40, 47)
assert getNewRange('F', 44, 45) == (44,44)
assert getNewRange('R', 0, 7) == (4, 7)
assert getNewRange('L', 4, 7) == (4, 5)


# Rules
# Rows
# F means to take the lower half
# B means to take the upper half
# range of rows = 0 - 127

# Columns
# L means lower half
# R means upper half
# range of columns = 0 - 7

# Assert
# seat ID = row * 8 + column
# FBFBBFFRLR  row 44, column 5, seat ID 357
# BFFFBBFRRR: row 70, column 7, seat ID 567
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820
