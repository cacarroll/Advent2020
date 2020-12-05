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