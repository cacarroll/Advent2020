# part 1
# want to find direct/indirect bags that will carry a gold bag

valid_bag_colors = []
def find_color_in_bag(color, input):
    # Input = muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    if color in input.split('contain')[1]:
        return (input.split(' ')[1])
        

input = "Day7\\input.txt"
color = 'gold'
directBags = []
with open(input) as file:
    rules = file.readlines()
    rules = [rule.split('\n')[0] for rule in rules]
    for rule in rules:
        colorFound = find_color_in_bag(color, rule)
        #print(colorFound)
        if colorFound != None and colorFound not in directBags:
            print(f"adding {colorFound} to directBags")
            directBags.append(colorFound)
    print(directBags)
    print(len(directBags))

    # now do any of these color belong in other bags
    newBagsAdded = ''
    while newBagsAdded != 0:
        for rule in rules:
            for color in directBags:
                colorFound = find_color_in_bag(color,rule)
                if colorFound != None and colorFound not in directBags:
                    newBagsAdded += 1
                    print(f"adding {colorFound} to directBags")
                    directBags.append(colorFound)
                else:
                    newBagsAdded = 0
            
    print(directBags)
    print(len(directBags))


        





#     Count = 0
#     test = ()
#     for rule in rules:
#         part1, part2 = (rule.split('contain')[0]),(rule.split('contain')[1])
#         #Direct
#         if 'gold' in part2:
#             Count +=1
#             print(rule)
#             direct = (rule.split(' ')[1])
#             #print(f'found it {direct}')

#             for indirect in rules:
#                 part3, part4 = (indirect.split('contain')[0]),(indirect.split('contain')[1])
#                 #print (f"part3: {part3} , part4: {part4}")
#                 print(f"We are looking for {direct} in {part3}")
#                 if direct in part3:
#                     print(f'found {direct} in {part3}" ')
#                 #     indirectColor = (part3.split(' ')[1])
#                 #     print(f'found indirect {indirectColor}')

