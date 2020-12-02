count = 0
def rule1(rule):
    count = 0
    occMin = int(rule.split(" ")[0].split("-")[0]); occMax = int(rule.split(" ")[0].split("-")[1])
    specialChar = rule.split(" ")[1].replace(':', " ").strip()
    password = rule.split(" ")[2]
    counter = str(password).count(specialChar)
    if counter <= occMax and counter >= occMin:
        return True


with open("input.txt") as file:
    rules = [str(line.rstrip()) for line in file]
    for rule in rules:
        result = rule1(rule)
        if result == True:
            count = count + 1
print(count)
