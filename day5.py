def readfile():
    file = open('C:/Users/venla/Documents/Koodaus/advent_of_code/day5.txt', 'r')
    order = file.read()
    moves = order.split('\n')
    lengthmoves = len(moves)
    message = []

    
    stucks = [["N", "R", "G", "P"], ["J", "T", "B", "L", "F", "G", "D", "C"], ["M", "S", "V"], ["L", "S", "R", "C", "Z", "P"], ["P", "S", "L", "V", "C", "W", "D", "Q"], ["C", "T", "N", "W", "D", "M", "S"], ["H", "D", "G", "W", "P"], ["Z", "L", "P", "H", "S", "C", "M", "V"], ["R", "P", "F", "L", "W", "G", "Z"]]
    
    #part 2

    for i in range (0, lengthmoves):
        command = moves[i].split(' ')
        howMany = int(command[1])
        fromStuck = int(command[3])
        toStuck = int(command[5])

        for n in range(0, howMany):
            lengthStuck = len(stucks[fromStuck -1])
            moveThis = stucks[fromStuck-1][lengthStuck-howMany+n] 
            stucks[toStuck-1].append(moveThis)
            stucks[fromStuck-1].pop(lengthStuck-howMany+n)
            
        
    for i in range (0, len(stucks)):    
        message.append(stucks[i][len(stucks[i])-1])

    print(message)



    """
    part 1
    for i in range (0, lengthmoves):
        command = moves[i].split(' ')
        howMany = int(command[1])
        fromStuck = int(command[3])
        toStuck = int(command[5])

        for n in range(0, howMany):
            lengthStuck = len(stucks[fromStuck -1])
            moveThis = stucks[fromStuck-1][lengthStuck-1]    
            stucks[toStuck-1].append(moveThis)
            stucks[fromStuck-1].pop(lengthStuck-1)
        
    for i in range (0, len(stucks)):    
        message.append(stucks[i][len(stucks[i])-1])

    print(message)
    """



readfile()    