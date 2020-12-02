def fuel(mass):
    return mass // 3 - 2


def fuel_for_the_fuel(mass: int) ->int:
    total = 0
    next_fuel = fuel(mass)
    while next_fuel > 0:
        #print(next_fuel,total)
        total += next_fuel
        next_fuel = fuel(next_fuel)
    return total

assert fuel(12) == 2
assert fuel(14) == 2
assert fuel(1969) == 654
assert fuel(100756) == 33583


with open("input.txt") as file:
    masses = [int(line.strip()) for line in file]
    part1 = sum(fuel(mass) for mass in masses)
    
assert fuel_for_the_fuel(14) == 2
assert fuel_for_the_fuel(1969) == 966
assert fuel_for_the_fuel(100756) == 50346

part2 = sum(fuel_for_the_fuel(mass) for mass in masses)

# print(masses)
print(part1)
print(part2)
ttl = part1 + part2
print(ttl)

# with open("input.txt") as file:
#     masses = [int(line.strip()) for line in file]

    