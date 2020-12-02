count = 0
def rule1(rule):
    count = 0
    occMin = int(rule.split(" ")[0].split("-")[0]); occMax = int(rule.split(" ")[0].split("-")[1])
    specialChar = rule.split(" ")[1].replace(':', " ").strip()
    password = rule.split(" ")[2]
    counter = str(password).count(specialChar)
    if counter <= occMax and counter >= occMin:
        return True
    else:
        return False


def rule2(rule):
    pos1 = (int(rule.split(" ")[0].split("-")[0]) -1); pos2 = (int(rule.split(" ")[0].split("-")[1]) -1)
    specialChar = rule.split(" ")[1].replace(':', " ").strip()
    
    password = str(rule.split(" ")[2])
    char1 = password[pos1]
    char2 = password[pos2]
    print(f"password: {password}, specialChar: {specialChar}, char1: {char1}, char2: {char2}, pos1: {pos1}, pos2: {pos2}")
    if (specialChar == char1 or specialChar == char2) and char1 != char2:
        return True
    else:
        return False


with open("input.txt") as file:
    rules = [str(line.rstrip()) for line in file]
    for rule in rules:
        result = rule2(rule)
        if result == True:
            count = count + 1
print(count)

#Part 1
pwd1 = '1-3 a: abcde'; assert rule1(pwd1) == True
pwd2 = '2-9 c: ccccccccc'; assert rule1(pwd2) == True
pwd3 = '1-3 b: cdefg'; assert rule1(pwd3) == False

# Part 2
pwd4 = '1-3 a: abcde'; assert rule2(pwd4) == True
pwd5 = '1-3 b: cdefg'; assert rule2(pwd5) == False
pwd6 = '2-9 c: ccccccccc'; assert rule2(pwd6) == False
pwd7 = '6-19 g: gggggggggggggggggggg'; assert rule2(pwd7) == False
