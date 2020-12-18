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


# part 2
def get_unique_answer_all(responses):
    questions = []
    inAllLines = True

    for char in responses[0]:
        inAllLines = True
        for line in responses:
            if char not in line:
                inAllLines = False

        if inAllLines and char not in questions:
            questions.append(char)
    
    return len(questions)


sum = 0
currentResponse = []
for line in cd:
    if line != '':
        currentResponse.append(line)
    else:
        sum += get_unique_answer_all(currentResponse)
        currentResponse = []

sum += get_unique_answer_all(currentResponse)
print(sum)