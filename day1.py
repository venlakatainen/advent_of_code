def readfile():
    file = open('C:/Users/venla/Documents/Koodaus/advent_of_code/day1.txt', 'r')
    calories = file.read()
    getcalories = calories.split('\n')
    lenght = len(getcalories)


    for i in range(0, lenght):
        if getcalories[i] == '':
            getcalories[i] = 0
        else:
            getcalories[i] = int(getcalories[i])


    sum = [0] * lenght
    j=0

    for i in range(lenght):
        if (getcalories[i] == 0):
            j += 1
            continue
        else:
            sum[j] = sum[j] + getcalories[i]
            

    biggest = max(sum)
    print(biggest)
    

readfile()
    