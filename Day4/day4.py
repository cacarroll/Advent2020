fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

# Rule 
def is_passport_valid(pp):
    for field in fields:
        if field not in pp:
            return False
    return True


with open("input.txt") as file:
    data = file.readlines()
    data = [line.strip() for line in data]
#print(data)
ValidCount = 0
currentPassport = ''
for line in data:
    if line != '':
        currentPassport += ' ' + line
    else:
        if is_passport_valid(currentPassport):
            ValidCount += 1
        currentPassport = ''

if is_passport_valid(currentPassport):
    ValidCount += 1

print(ValidCount)


pp1 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
pp2 = "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929"
pp3 = "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm"
pp4 = "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"

assert is_passport_valid(pp1) == True
assert is_passport_valid(pp2) == False
assert is_passport_valid(pp3) == True
assert is_passport_valid(pp4) == False
