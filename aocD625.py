def init(data, rows, columns):
    list_ = []
    length = 0
    for i in range(rows-1):
        list_.append(data[length:(columns//rows)+length])
        length += columns//rows
        i+=1
    operation = data[length:(columns//rows)+length]
    return list_, operation

def init2(data, rows, columns):
    list_ = []
    length = 0
    print(len(data))
    for i in range(rows-1):
        list_.append(data[length:(columns//rows)+length])
        length += columns//rows
        i+=1
    operation = data[-1].split()
    return list_, operation

def p1(list_, operation):
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
    #print("Total:", total)

def mathh(list, last, current, index, operation):
    print("Detected Operation:", operation[index], last, current)
    total = 0
    if operation[index] == "+":
        total =0 
        print("+")
    elif operation[index] == "*":
        total = 1
        print("*")

    #make the numbers:
    for j in range(last, current):
        number = list[0][0][j] #initalise the first "number" in the column 
        #print("Number Added:", list[0][0][j], "Row: 0")
        for i in range(1, len(list)): #fully make the number in the column
            number += list[i][0][j]
            #print("Number Added:", list[i][0][j], "Row:", i)
        number = int(number) #convert to interger
        print("Column:",j, "Number", number)
        if operation[index] == "+":
            total += number
        elif operation[index] == "*":
            total = total*number
        print("Current Total:", total)
    print("Individual Total:", total)
    return total

def p2(list_, operation):
    index = 0
    total = 0

    #first check to ensure that there is the same number of chrs per string in the list_
    for i in range(0, len(list_)):
        if len(list_[i-1][0]) != len(list_[i][0]):
            print("Invalid Lists")
            break    
        else:
            #print("Valid lists;", i, len(list_[i][0]))
            continue
    last = 0
    for j in range(0, len(list_[0][0])): #second we need to determine where our math problem begins and ends, 0 -> legnth of str len(list_[0][0])
        #print("Checking Column:", j)
        space_detected = 0
        for i in range(0, len(list_)): #the column we on
            #print(list_[i][0], list_[i][0][j], i, j)
            if list_[i][0][j] == " ": #detect a space
                space_detected +=1
                #print("Space Detected")
            elif j == (len(list_[0][0])-1):
                #print("Math Detected at Space:", j+1)
                #print("ELIF")
                total += mathh(list_, last, j+1, index, operation)
            else:
                continue
            if space_detected == len(list_):
                #print("Math Detected at Space:", j)
                total += mathh(list_, last, j, index, operation)
                index += 1
                last  = j +1        
    
    print("OOga Booga Total:", total)       
    return

with open("testD6.txt", "r") as file:
    everything = file.read()
    rows = everything.split("\n")
    everything = everything.split()
    #print(len(rows))
    #print(rows)
    list_, operation = init(everything, len(rows), len(everything))
    list2, operation2 = init2(rows, len(rows), len(rows))
    #print(operation2)
    p1(list_, operation)
    p2(list2, operation2)
    #print(list2)
    #print(operation)
    #print(len(list_[0]))
    #####################################################################
    
    