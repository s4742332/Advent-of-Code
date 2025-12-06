with open("testD6.txt", "r") as file:
    everything = file.read().split()
    one = everything[0:len(everything)//4]
    two = everything[len(everything)//4:len(everything)//2]
    three = everything[len(everything)//2:3*(len(everything)//4)]
    operation = everything[3*(len(everything)//4):len(everything)]

    #print(one)
    #print(two)
    #print(three)
    #print(operation)
    total = 0
    for i in range(0, len(one)):
        if operation[i] == "+":
            total += int(one[i]) +int(two[i])+int(three[i])
            #print("Added:",one[i], two[i],three[i]) 
        elif operation[i] == "*":
            total += int(one[i]) *int(two[i])*int(three[i])
            #print("Multiplied:",one[i], two[i],three[i]) 
        else:
            print("No Operation")
    print("Total:", total)
    