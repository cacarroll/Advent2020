count = 0

with open("input.txt") as file:
    rules = [str(line.rstrip()) for line in file]
    #rule = '4-14 d: lxdmddfddddddd'
    for rule in rules:
        occMin = int(rule.split(" ")[0].split("-")[0]); occMax = int(rule.split(" ")[0].split("-")[1])
        specialChar = rule.split(" ")[1].replace(':', " ").strip()
        password = rule.split(" ")[2]
        # print(f"occMin = {occMin}")
        # print(f"occMax = {occMax}")
        # print(f"Special Char = {specialChar}")
        # print(f"Password= {password}")
        counter = str(password).count(specialChar)
        if counter <= occMax and counter >= occMin:
            count = count + 1
print(count)
