def add(x, y, z=0):
    if x + y + z == 2020:
        print(f"{x} plus {y} plus {z} equals 2020")
        multiply(x, y, z)


def multiply(x, y, z):
    if z == 0:
        result = x * y
    else:
        result =  x * y * z
    print(result)


with open('input.txt') as file:
    entries = [int(line.rstrip()) for line in file]
    for x in entries:
        for y in entries:
            add(x, y)
            for z in entries:
                add(x, y, z)




