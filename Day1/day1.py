with open('input.txt') as file:
    entries = [int(line.rstrip()) for line in file]
    for e in entries:
        for y in entries:
            if e + y == 2020:
                print(f"{e} plus {y} equals 2020")
                result = e * y
                print(f"{e} multiplied by {y} equals {result}")
                break



