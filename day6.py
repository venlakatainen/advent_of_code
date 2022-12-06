def readfile():
    file = open('C:/Users/venla/Documents/Koodaus/advent_of_code/day6.txt', 'r')
    signal = file.read()
    signalLength = len(signal)
    
    for i in range(0,signalLength-14):    
         
        char1 = signal[i]  
        char2 = signal[i+1]
        char3 = signal[i+2]
        char4 = signal[i+3]
        char5 = signal[i+4]
        char6 = signal[i+5]
        char7 = signal[i+6]
        char8 = signal[i+7]
        char9 = signal[i+8]
        char10 = signal[i+9]
        char11 = signal[i+10]
        char12 = signal[i+11]
        char13 = signal[i+12]
        char14 = signal[i+13]
        
        if (char1 != char2) and (char1 != char3) and (char1 != char4) and (char1 != char5) and (char1 != char6) and (char1 != char7) and (char1 != char8) and (char1 != char9) and (char1 != char10) and (char1 != char11) and (char1 != char12) and (char1 != char13) and (char1 != char14):
            
            if (char2 != char3) and (char2 != char4) and (char2 != char5) and (char2 != char6) and (char2 != char7) and (char2 != char8) and (char2 != char9) and (char2 != char10) and (char2 != char11) and (char2 != char12) and (char2 != char12) and (char2 != char14):
            
                if (char3 != char4) and (char3 != char5) and (char3 != char6) and (char3 != char7) and (char3 != char8) and (char3 != char9) and (char3 != char10) and (char3 != char11) and (char3 != char12) and (char3 != char12) and (char3 != char14): 
                    
                    if (char4 != char5) and (char4 != char6) and (char4 != char7) and (char4 != char8) and (char4 != char9) and (char4 != char10) and (char4 != char11) and (char4 != char12) and (char4 != char13) and (char4 != char14):
                        
                        if (char5 != char6) and (char5 != char7) and (char5 != char8) and (char5 != char9) and (char5 != char10) and (char5 != char11) and (char5 != char12) and (char5 != char12) and (char5 != char14):

                            if (char6 != char7) and (char6 != char8) and (char6 != char9) and (char6 != char10) and (char6 != char11) and (char6 != char12) and (char6 != char13) and (char6 != char14):

                                if (char7 != char8) and (char7 != char9) and (char7 != char10) and (char7 != char11) and (char7 != char12) and (char7 != char13) and (char7 != char14): 
                                    
                                    if (char8 != char9) and (char8 != char10) and (char8 != char11) and (char8 != char12) and (char8 != char13) and (char8 != char14):
                                        
                                        if (char9 != char10) and (char9 != char11) and (char9 != char12) and (char9 != char13) and (char9 != char14):

                                            if (char10 != char11) and (char10 != char12) and (char10 != char13) and (char10 != char14):

                                                if (char11 != char12) and (char11 != char13) and (char11 != char14):

                                                    if (char12 != char13) and (char12 != char14):

                                                        if (char13 != char14):
                                                            print(i+14)    
                                                            break


    """
    part1   
    for i in range(0,signalLength-4):
        char1 = signal[i]  
        char2 = signal[i+1]
        char3 = signal[i+2]
        char4 = signal[i+3]
        
        if (char1 != char2) and (char1 != char3) and (char1 != char4):
            
            if (char2 != char3) and (char2 != char4):
            
                if (char3 != char4): 
                    print(i+4)    
                    break
    """    
                

readfile()