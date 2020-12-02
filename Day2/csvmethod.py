import csv

with open("input.csv") as data:
    reader = csv.reader(data, delimiter= ' ')

    ValidCount = 0
    ValidCount2 = 0
    for row in reader:
        quota, letter, pw = row[0], row[1][0], row[2]
        #print(quota, letter, pw)

        i = quota.index('-')
        lower = int(quota[:i])
        upper = int(quota[i+1:])

        count = 0
        for character in pw:
            if character == letter:
                count += 1
        if count >= lower and count <=upper:
            ValidCount += 1

        first = pw[lower-1] == letter
        last = pw[upper-1] == letter

        if (first and not last) or (last and not first):
            ValidCount2 += 1

print(f"Part One answer: {ValidCount}")
print(f"Part two answer: {ValidCount2}")
