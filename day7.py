def readfile():
    file = open('C:/Users/venla/Documents/Koodaus/advent_of_code/day7.txt', 'r')
    commands = file.read().split('\n')
    countOfCommands = len(commands)
    #print(commands)
    directories = []
    subdirectories = []
    sizes = [0] * 500
    directories.append("/")
    currentDir = 0
    

    
    for i in range(countOfCommands):
        command = commands[i].split(' ')
        print(command)

        if command[0] == "$":
            print("$")
            
            if command[1] == "cd":
                print("cd")
                
                if command[2] == "..":
                    print("one back")
                    if currentDir == 0:
                        continue
                    else:
                        currentDir -= 1
                
                elif command[2] == "/":
                    currentDir = 0
                
                else :
                    for j in range(len(directories)):
                        if directories[j] == command[2]:
                            index = j
                            break
                        input()
                    currentDir = index

            if command[1] == "ls":
                print("ls")


        elif command[0]=="dir":
            print("dir")
            if command[1] in directories:
                print("founded")
                
            else:
                directories.append(command[1])
                print(directories)
        
        else :
            print(currentDir)
            print(command)
            print(command[0])
            print(sizes)
            sizes[currentDir] += int(command[0])
        
        print(directories)
        print(sizes)
        print(currentDir)
        input()

    print(directories)
    print(sizes)
    sum = 0
    for m in range(len(sizes)):
        if (int(sizes[m]) <= 100000):
            sum += sizes[m]
        
    print(sum)

readfile()