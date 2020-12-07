def is_passport_valid(pp):
    fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    for field in fields:
        if field not in pp:
            #print(field, pp)
            return False
    return True


def is_valid_height(hgt):
    if hgt.endswith('cm'):
        value = int(hgt[:-2])
        if value >= 150 and value <=193:
            return True
    elif hgt.endswith('in'):
        value = int(hgt[:-2])
        if value >= 59 and value <=76:
            return True
    else:
       return False


def is_valid_hair_color(hcl):
    if hcl[0] == '#' and len(hcl) == 7 and not any([c not in '0123456789abcdef' for c in hcl[1:]]):
        return True


def is_valid_eye_color(ecl):
    ValidEyeColor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in ValidEyeColor:
        return True


def is_valid_pid(pid):
    if len(pid) == 9:
       return True


def is_valid_date(date:int,min:int,max:int):
    if len(date) == 4 and int(date) >= int(min) and int(date) <=int(max):
        return True


def is_valid_passport_data(ValidPassport):
    ValidPassport = ValidPassport.split()
    data = {}
    for item in ValidPassport:
        key = item[:3]
        value = item[4:]
        data[key] = value
    if is_valid_pid(data['pid']) and is_valid_hair_color(data['hcl']) and is_valid_height(data['hgt']) and is_valid_date(data['byr'],1920, 2002) and is_valid_date(data['iyr'],2010, 2020) and is_valid_date(data['eyr'],2020, 2030):
        return True
    else:
        return False

CurrentPassport = ''
ValidPassports = []
ValidCount = 0
ValidData = 0
with open('Day4\\input.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    for line in data:
        if line != '':
            CurrentPassport += ' ' + line

        else:
            if is_passport_valid(CurrentPassport):
                ValidCount += 1
                ValidPassports.append(CurrentPassport)
            CurrentPassport = ''

    if is_passport_valid(CurrentPassport):
        ValidCount += 1
        ValidPassports.append(CurrentPassport)
        
print(f"This is our valid count: {ValidCount}")


list = []
data = {}
VerifiedPassports = 0
for pp in ValidPassports:
    pp = pp.split()
    for item in pp:
        key = item[:3]
        value = item[4:]
        data[key] = value
        list.append(data)

    if is_valid_height(data['hgt']) and is_valid_eye_color(data['ecl']) and is_valid_hair_color(data['hcl']) and is_valid_pid(data['pid']) and is_valid_date(data['byr'],1920, 2002) and is_valid_date(data['iyr'],2010, 2020)  and is_valid_date(data['eyr'],2020, 2030):
        VerifiedPassports +=1

print(f"Valid Data Count {VerifiedPassports}")
        

# Part 1 Assert
pp1 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
pp2 = "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929"
pp3 = "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm"
pp4 = "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"
assert is_passport_valid(pp1) == True
assert is_passport_valid(pp2) == False
assert is_passport_valid(pp3) == True
assert is_passport_valid(pp4) == False

# part 2 Assert
pp5 = "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"
pp6 = "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946"
pp7 = "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"
pp8 = "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007"
assert is_valid_passport_data(pp5) == False
assert is_valid_passport_data(pp6) == False
assert is_valid_passport_data(pp7) == False
assert is_valid_passport_data(pp8) == False

pp9 = "pid:087499704 cid:100 hcl:#18171d"
pp10 = "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"
pp11 = "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022"
pp12 = "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"

#assert is_valid_passport_data(pp9) == True
assert is_valid_passport_data(pp10) == True
assert is_valid_passport_data(pp11) == True
assert is_valid_passport_data(pp12) == True
