
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
    #print("IDs:", IDs)
    return ranges, IDs

def total_possible_fresh(ranges):
    all_ranges = []
    total = 0
    for i in range(1, len(ranges),2): #need to rearrange the info for sorting properly
        all_ranges.append((int(ranges[i-1]), int(ranges[i])))
    all_ranges.sort() #rearrange so that all the ranges are in order
    
    current_highest = -1
    for a,b in all_ranges: #for a given range in all_ranges
        if current_highest>=a: #are we starting inside a previously investigated range?
            a = current_highest +1  #start at the next unseen number
        if a<=b: #if it is in the range, and there is stuff new in the range we haven't seen it before
            total += b-a +1 # add the total numbers in any given range
        current_highest = max(current_highest,b) #ensure that current is updated to the end of the interval
    return total

with open("groceries.txt", "r") as file:
    everything = file.read().split('\n') #seperate by liens
    ranges, IDs = get_ranges(everything)
    fresh =0
    spoiled = 0
    list_fresh = []
    list_spoiled = []

    for id in IDs:
        #print(id)
        k = int(id)
        place = IDs.index(id)
        for i in range(1, len(ranges),2):
            if int(ranges[i-1]) <= k < (int(ranges[i])+1):
                fresh +=1
                #print("Fresh:", int(ranges[i-1]),int(ranges[i]),":", id)
                list_fresh.append(id)
                #IDs.pop(place)
                break
            else:
                #print("Spoiled:",int(ranges[i-1]),int(ranges[i]),":", id)
                continue
        if id not in list_fresh:
            list_spoiled.append(id)
    #print(hasduplicates(sorted(list_fresh))) proves no duplicates in list
    #print("All IDs:", IDs)
    #print("All Fresh:", list_fresh)
    #print("All Spoiled:", list_spoiled)
    #print("Total Fresh", fresh)
    print(total_possible_fresh(ranges))
            

            

    
    
