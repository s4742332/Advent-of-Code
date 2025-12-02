"""
To extract the Data into aoc.txt Steps in obsidian
"""
code = 0

with open("IDs.txt", "r") as file:
    allcode = file.read() # Read file
    all_IDs = allcode.split(',') #split ID Ranges
    for id in all_IDs: #For each ID Range
        first_ID, last_ID = id.split('-') #First and last ID
        full_ID = range(int(first_ID), (int(last_ID)+1)) #Range between IDs
        for full_number in full_ID: #For each inidividual number in the range of IDS
                full_number = str(full_number) #conver to string
                found = False
                for size in range(1, len(full_number)//2+1): #checks for each size of number inside the full number
                    if len(full_number)%size!=0: 
                          continue
                    block = full_number[:size] #different blocks of numbers from original number

                    if block * (len(full_number)//size) == full_number: #check if the entire string is the block repeated by a number of times
                        print(full_number)
                        code += int(full_number)
                        found = True
                        break
                   
                
print(code)
                                 
                                 
                                
                

