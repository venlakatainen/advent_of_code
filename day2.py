
def readfile():
    file = open('C:/Users/venla/Documents/Koodaus/advent_of_code/day2.txt', 'r')
    moves = file.read()
    round = moves.split('\n')
    length = len(round)
    
    game = []

    for i in range(0, length):
       tuple = round[i].split(' ')
       game.append(tuple)

    # A = rock 
    # B = paper
    # C = scissors

    # X = rock
    # Y = paper
    # Z = scissors
    me = 0
    total = 0
    for j in range(0, length):
        if game[j][1] == "X":    # rock
            me += 1
            if game[j][0] == "A": # rock (draw)
                me +=3
            
            elif game[j][0] == "B": # paper (lose)
                me += 0

            elif game[j][0] == "C": # scissors (win)
                me += 6
        
        elif game[j][1] == "Y": # paper
            me += 2
            if game[j][0] == "A":  # rock (win)
                me += 6
            
            elif game[j][0] == "B": # paper (draw)
                me += 3

            elif game[j][0] == "C": # scissors (lose)
                me += 0
        
        elif game[j][1] == "Z": # scissors
            me += 3
            if game[j][0] == "A": # rock (lose)
                me += 0

            elif game[j][0] == "B": # paper (win)
                me += 6

            elif game[j][0] == "C": # Scissors (draw)
                me += 3

    #print(me)

    for j in range(0, length):
        if game[j][0] == "A":    # rock
            
            if game[j][1] == "X": # lose
                total +=0   #lose
                total +=3   #scissors
            
            elif game[j][1] == "Y": # draw
                total += 3  #draw
                total += 1  #rock

            elif game[j][1] == "Z": # win
                total += 6  #win
                total += 2  #paper
        
        elif game[j][0] == "B": # paper
            
            if game[j][1] == "X":  # lose
                total += 0  #lose
                total += 1  #rock
            
            elif game[j][1] == "Y": # draw
                total += 3  #draw
                total += 2  #paper

            elif game[j][1] == "Z": # win
                total += 6  #win
                total += 3  #scissors
        
        elif game[j][0] == "C": # scissors
            
            if game[j][1] == "X": # lose
                total += 0  #lose
                total += 2  #paper

            elif game[j][1] == "Y": # draw
                total += 3  #draw
                total += 3  #scissors

            elif game[j][1] == "Z": # win
                total += 6  #win
                total += 1  #rock
    
    print(total)
    

readfile()