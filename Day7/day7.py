
input = "Day7\\input.txt"

with open(input) as file:
    data = file.readlines()
    data = [line.strip() for line in data] 

def get_num_bags(color):
    lines = [ line for line in data if color in line and line.index(color) !=0 ]

    allColors = []

    if len(lines) == 0:
        return []
    else:
        colors = [ line[:line.index(' bags')] for line in lines]
        colors = [ color for color in colors if color not in allColors]
        
        for color in colors:
            allColors.append(color)
            bags = get_num_bags(color)    

            allColors += bags
        
        uniqueColars =  []
        for color in allColors:
            if color not in uniqueColars:
                uniqueColars.append(color)

        return uniqueColars


colors = get_num_bags('shiny gold')
print(len(colors))

