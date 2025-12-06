def init(data, rows, columns):
    list_ = []
    length = 0
    for i in range(rows-1):
        list_.append(data[length:(columns//rows)+length])
        length += columns//rows
        i+=1
    operation = data[length:(columns//rows)+length]
    return list_, operation

with open("testD6.txt", "r") as file:
    everything = file.read()
    rows = everything.split("\n")
    everything = everything.split()
    #print(len(rows))
    list_, operation = init(everything, len(rows), len(everything))
    #print(list_)
    #print(operation)
    #print(len(list_[0]))
    total = 0
    for i in range(0, len(list_[0])):
        if operation[i] == "+":
            current = 0
            for j in list_:
                current += int(j[i])
            #total += int(one[i]) +int(two[i])+int(three[i])
            #print("Added:",one[i], two[i],three[i]) 
            total+=current
            continue
        elif operation[i] == "*":
            current = 1
            for j in list_:
                current = current * int(j[i])
            #total += int(one[i]) *int(two[i])*int(three[i])
            #print("Multiplied:",one[i], two[i],three[i]) 
            total+=current
            continue
        else:
            #print("No Operation:",one[i], two[i],three[i])
            continue
    print("Total:", total)
    