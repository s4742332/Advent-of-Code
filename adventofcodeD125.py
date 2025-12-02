"""
To extract the Data into aoc.txt Steps in obsidian
"""

#Assign a name ot the input file
dial = 50 #Start at 50
answer = 0
answer_part1 = 0 #intial 0 count for part 1
answer_part2 = 0#intial 0 count for part 1


with open("aoc.txt", "r") as file:
    allcode = file.read() # Read file
    for i in range(len(allcode.split())): 
        line = allcode.split().pop(i)
        direction = line[0]
        clicks = int(line[1:])

        for no in range(clicks): #Move per click    
            if direction == "L": #move dial
                dial = (dial-1+100)%100 #keep track of the dial by moving incrementally
            else:
                dial = (dial+1)%100
            if dial==0: #Crosses over 0
                answer_part2+=1
        if dial==0: #Ends final movement at 0
                answer_part1+=1
    

print("answer part 1:", answer_part1)
print("answer part 2:", answer_part2)
        

