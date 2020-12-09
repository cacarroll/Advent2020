sampleData = "Day6\input.txt"

def sum_unique(response):
    unique = []
    for c in response:
        if c not in unique:
            unique +=c
    # print(unique)
    return len(unique)


with open(sampleData) as file:
    #split on the new line
    cd = file.readlines()
    cd = [line.strip() for line in cd]
    #print(cd)

sum = 0
response = ''
for line in cd:
    if line != "":
        response += line

    else:
        #print(response)
        sum += sum_unique(response)
        response = ''

sum += sum_unique(response)
print(sum)

