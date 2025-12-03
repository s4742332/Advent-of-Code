output = 0

with open("testD3.txt", "r") as file:
    allbanks = file.read().split() # Read file, convert to list of str
    alljoltage = []
    for bank in allbanks: #for each battery bank
        bank_joltage = []
        for i in range(0, len(bank)): #check every battery 
            for j in range((i+1), len(bank)): #against every battery after it 
                joltage = str(bank[i])+str(bank[j]) #what's the joltage of the two str together
                bank_joltage.append(int(joltage)) #append to list of joltages for this bank
        alljoltage.append(int(sorted(bank_joltage, reverse=True)[0])) #sort and append the highest value as an interger
        print(sorted(bank_joltage, reverse=True)[0], "For bank:", bank)   
        bank_joltage.clear()

    output = sum(alljoltage)
    print("Answer:", output)

              

