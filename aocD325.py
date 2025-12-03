output = 0

with open("testD3.txt", "r") as file:
    allbanks = file.read().split() # Read file, convert to list of str
    alljoltage = []
    for bank in allbanks: #for each battery bank
        bank_joltage = []
        for a in range(0, len(bank)):
            for b in range(a+1, len(bank)):
                for c in range(b+1, len(bank)):
                    for d in range(c+1, len(bank)):
                        for e in range(d+1, len(bank)):
                            for f in range(e+1, len(bank)):
                                for g in range(f+1, len(bank)):
                                    for h in range(g+1, len(bank)):
                                        for i in range(h+1, len(bank)):
                                            for j in range(i+1, len(bank)):
                                                for k in range(j+1, len(bank)):
                                                    for l in range(k+1, len(bank)):
                                                        joltage = str(bank[a]+bank[b]+bank[c]+bank[d]+bank[e]+bank[f]+bank[g]+bank[h]+bank[i]+bank[j]+bank[k]+bank[l])
                                                        bank_joltage.append(int(joltage))
        alljoltage.append(sorted(bank_joltage, reverse=True)[0]) #append the highest bank voltage, then turn to string to cut off the remining length
        print(sorted(bank_joltage, reverse=True)[0], "For bank:", bank)
        bank_joltage.clear()

    output = sum(alljoltage)
    print("Answer:", output)

              

