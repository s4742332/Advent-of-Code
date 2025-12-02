"""
To extract the Data into aoc.txt Steps in obsidian
"""

#Assign a name ot the input file
dial = 50 #Start at 50
answer = 0 #intial 0 count

with open("aoc.txt", "r") as file:
    allcode = file.read()
    print("lines:", (len(allcode.split())))
    for i in range(len(allcode.split())):
        line = allcode.split().pop(i)
        direction = line[0]
        clicks = int(line[1:])

        if direction == "L": #move dial
            dial = (dial-clicks+100)%100 
        else:
            dial = (dial+clicks)%100
        
        if dial==0:
            answer+=1
        
        print(clicks, dial, answer)


print("answer:", answer)
        

