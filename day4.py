def readfile():
    file = open('C:/Users/venla/Documents/Koodaus/advent_of_code/day4.txt', 'r')
    areas = file.read()
    pairs = areas.split('\n')
    lengthall = len(pairs)
    elves = []
    includes = 0
    

    for i in range(0, lengthall):
        tuples = pairs[i].split(",")
        elves.append(tuples)

    #part2

    for j in range(0, len(elves)):
        firstArea = elves[j][0]
        firstStart, firstEnd = firstArea.split("-")
        
        secondArea = elves[j][1]
        secondStart, secondEnd = secondArea.split("-")

        if ((int(firstStart) <= int(secondStart)) and (int(firstEnd) >= int(secondEnd))):
            includes = includes +1

        
        elif ((int(secondStart) <= int(firstStart)) and (int(secondEnd) >= int(firstEnd))):
            includes = includes +1

        
        elif ((int(firstStart) <= int(secondStart) <= int(firstEnd)) or (int(secondStart) <= int(firstStart) <= int(secondEnd))):
            includes = includes +1

        
        elif ((int(firstStart) <= int(secondEnd) <= int(firstEnd)) or (int(secondStart) <= int(firstEnd) <= int(secondEnd))):
            includes = includes +1


        elif ((int(secondEnd) == int(firstStart)) or (int(secondStart) == int(firstEnd))):
            includes = includes +1

    """
    part 1
    for j in range(0, len(elves)):
        firstArea = elves[j][0]
        firstStart, firstEnd = firstArea.split("-")
        
        secondArea = elves[j][1]
        secondStart, secondEnd = secondArea.split("-")

        if ((int(firstStart) <= int(secondStart)) and (int(firstEnd) >= int(secondEnd))):
            includes = includes +1
        
        elif ((int(secondStart) <= int(firstStart)) and (int(secondEnd) >= int(firstEnd))):
            includes = includes +1
    """
    print(includes)
    

    

readfile()