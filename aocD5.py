
def get_ranges(everything):
    ranges = []
    for x in everything:
        #print(x)
        if x == '':
            IDs = everything[(everything.index(x)+1):len(everything)]
            #print("Ranges over")
            break
        else:
            for y in range(0,len(x)):
                if x[y] == '-':
                    ranges.append(int(x[0:(y)]))
                    ranges.append(int(x[(y+1):len(x)]))
                else: continue
    print("Ranges:", ranges)
    print("IDs:", IDs)
    return ranges, IDs


with open("testD5.txt", "r") as file:
    everything = file.read().split('\n') #seperate by liens
    ranges, IDs = get_ranges(everything)
    fresh =0
    spoiled = 0
    for i in range(1, len(ranges), 2):
        for id in IDs:
            k =int(id)
            place = IDs.index(id)
            if k in range(ranges[i-1], (ranges[i]+1)):
                fresh +=1
                print("Fresh:", ranges[i-1], ranges[i],":", id)
                IDs.pop(place)
            else:
                print("Spoiled:", ranges[i-1], ranges[i],":", id)
    print("Total Fresh", fresh)

    
    
