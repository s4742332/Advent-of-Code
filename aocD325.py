output = 0
first_part = 0

 
with open("testD3.txt", "r") as file:
    allbanks = file.read().split() # Read file, convert to list of str
    alljoltage = []
    first_part_alljoltage = []
    #for bank in allbanks: #for each battery bank
    bank_joltage = []
    first_part_bank_joltage = []
    for bank in allbanks:
        for a in range(0, len(bank)):
            for b in range(a+1, len(bank)):
                first_part_joltage = str(bank[a]+bank[b])
                first_part_bank_joltage.append(int(first_part_joltage))

        first_part_alljoltage.append(sorted(first_part_bank_joltage, reverse=True)[0]) #append the highest bank voltage, then turn to string to cut off the remining length
        print(sorted(first_part_bank_joltage, reverse=True)[0], "For bank:", bank)
        first_part_bank_joltage.clear()                            

    first_part = sum(first_part_alljoltage)
    output = sum(alljoltage)
    print("Answer Part 1:", first_part)
    print("Answer Part 2:", output)


              

