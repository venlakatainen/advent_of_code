def readfile():
    file = open('C:/Users/venla/Documents/Koodaus/advent_of_code/day1.txt', 'r')
    calories = file.read()
    getcalories = calories.split('\n')
    length = len(getcalories)


    for i in range(0, length):
        if getcalories[i] == '':
            getcalories[i] = 0
        else:
            getcalories[i] = int(getcalories[i])


    sum = [0] * length
    j=0

    for i in range(length):
        if (getcalories[i] == 0):
            j += 1
            continue
        else:
            sum[j] = sum[j] + getcalories[i]
            

    biggest = max(sum)
    reverse = sorted(sum, reverse=True)
    topthree = reverse[0] + reverse[1] + reverse[2]

    print(topthree)
    print(biggest)
    

readfile()
    