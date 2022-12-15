def readfile():
    file = open('C:/Users/venla/Documents/Koodaus/advent_of_code/day8.txt', 'r')
    rows = file.read().split('\n')
    countOfRows = len(rows)
    score = 0

    # part2
    for j in range(1, countOfRows-1):
        # one row
        row = rows[j]
        
        for n in range(1, len(row)-1):
            counting = 0
            canSeeLeft = 0
            canSeeRight = 0
            canSeeUp = 0
            canSeeDown = 0

            # one mark from row
            tree = int(row[n])
            
            # how many trees can bee seen on the left side
            for m in reversed(range(0, n)):
                if int(tree) > int(row[m]):
                  canSeeLeft += 1
                else:
                    canSeeLeft += 1
                    break
            

            # how many trees can bee seen on the right side               
            for k in range(n+1, len(row)):
                if int(tree) > int(row[k]):
                    canSeeRight += 1
                else:
                    canSeeRight += 1
                    break
            
            # how many trees can bee seen on the upper side        
            for l in reversed(range(0, j)):
                if int(tree) > int(rows[l][n]):
                    canSeeUp += 1
                else:
                    canSeeUp += 1
                    break
            
            # how many trees can bee seen down         
            for s in range(j+1, countOfRows):
                if int(tree) > int(rows[s][n]):
                    canSeeDown += 1   
                else:
                    canSeeDown += 1
                    break

            counting = canSeeLeft * canSeeRight * canSeeDown * canSeeUp
            
            if int(counting) > int(score):
                score = counting

    print(score)

    """
    part1
    visible = len(rows[0]) + len(rows[countOfRows-1]) + (2*(countOfRows-2))

    for j in range(1, countOfRows-1):
        # one row
        row = rows[j]
        #print(row)
        
        for n in range(1, len(row)-1):
            
            visibleLeft = 0
            visibleRight = 0
            visibleUp = 0
            visibleDown = 0
            
            # one mark from row
            tree = int(row[n])
            
            for m in range(0, n):
                if int(tree) > int(row[m]):
                  visibleLeft += 1
                else:
                    break
                
                
            if (visibleLeft == n):
                visible += 1
                continue
                           
            for k in range(n+1, len(row)):
                if int(tree) > int(row[k]):
                    visibleRight += 1
                else:
                    break
                
            if (visibleRight == len(row)-n-1):
                visible += 1
                continue

            #check if visible upper side    
              
            for l in range(0, j):
                if int(tree) > int(rows[l][n]):
                    visibleUp += 1
                else:
                    break

            if (visibleUp == j):
                visible += 1

            #check if visible lower side      
            for s in range(j+1, countOfRows):
                if int(tree) > int(rows[s][n]):
                    visibleDown += 1   
                else:
                    break
             
            if (visibleDown == (countOfRows-1-j)):
                visible += 1
                
    print(visible)
   """

readfile()