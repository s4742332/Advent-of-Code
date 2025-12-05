
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
    list_fresh = []
    list_spoiled = []

    for id in IDs:
        print(id)
        k = int(id)
        place = IDs.index(id)
        for i in range(1, len(ranges),2):
            if int(ranges[i-1]) <= k < (int(ranges[i])+1):
                fresh +=1
                print("Fresh:", int(ranges[i-1]),int(ranges[i]),":", id)
                list_fresh.append(id)
                #IDs.pop(place)
                break
            else:
                print("Spoiled:",int(ranges[i-1]),int(ranges[i]),":", id)
                continue
        if id not in list_fresh:
            list_spoiled.append(id)
    #print(hasduplicates(sorted(list_fresh))) proves no duplicates in list
    print("All IDs:", IDs)
    print("All Fresh:", list_fresh)
    print("All Spoiled:", list_spoiled)
    print("Total Fresh", fresh)
            

            

    
    
