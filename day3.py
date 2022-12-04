def readfile():
    file = open('C:/Users/venla/Documents/Koodaus/advent_of_code/day3.txt', 'r')
    allsacks = file.read()
    sack = allsacks.split('\n')
    lengthall = len(sack)
    sum = 0
    prior1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    

    groups = [sack[x:x+3] for x in range(0, lengthall, 3)]
    #print(groups)
  

    #part 2
    for count in range(0,len(groups)):
        for group in range(0,3):
            if group == 0:
                team1 = groups[count][group]
            elif group == 1:
                team2 = groups[count][group]
            elif group == 2:
                team3 = groups[count][group]
        

        len1 = len(team1)
        len2 = len(team2)
        len3 = len(team3)

       
        max = 0

        if (len1 > max):
            max = len1
 
        if (len2 > max):
            max = len2
       
        if (len3 > max):
            max = len3
        


        for marks in range(0, max):
            
            if (team1[marks] in team2) and (team1[marks] in team3):
                priority = team1[marks]
                
                if priority in prior1:
                    index = prior1.index(priority)
                    print(index)
                    sum += index + 1
                    
                    break
                else:
                    print("problems")

    print(sum)
    """
    part 1
    for num in range(0, lengthall):
        onesack = sack[num]
        length = len(sack[num])
        print(onesack)
        #print(length)
        first = []
        second = []
        for sad in range(0, length):
            #print(length//2)
            if (sad < (length/2)):
                first.append(onesack[sad])
            elif (sad >= (length/2)):
                second.append(onesack[sad])

        print(first)
        print(second)
        
        for mark in range(0, (length//2)):
            if (first[mark] in second):
                priority = first[mark]
                print(priority)
                if priority in prior1:
                    index = prior1.index(priority)
                    print(index)
                    sum += index + 1
                    print(sum)
                    break
                else:
                    print("problems")
            
    print(sum)
    """

readfile()

