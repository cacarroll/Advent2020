from calc import add, multiply

with open('input.txt') as file:
    entries = [int(line.rstrip()) for line in file]
    for x in entries:
        for y in entries:
            result = add(x, y)
            if result == 2020:
                print(f"{x} plus {y} = 2020")
                multiply(x, y)
            for z in entries:
                result = add(x, y, z)
                if result == 2020:
                    print(f"{x} plus {y} plus {z} = 2020")
                    result = multiply(x, y, z)
                    print(f"Multiplied equals {result}")