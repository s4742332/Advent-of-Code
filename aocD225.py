"""
To extract the Data into aoc.txt Steps in obsidian
"""
code = 0

with open("testD2.txt", "r") as file:
    allcode = file.read() # Read file
    all_IDs = allcode.split(',') #split ID Ranges
    for id in all_IDs: #For each ID Range
        first_ID, last_ID = id.split('-') #First and last ID
        full_ID = range(int(first_ID), (int(last_ID)+1)) #Range between IDs
        for full_number in full_ID: #For each inidividual number in the range of IDS
                full_number = str(full_number) #conver to string
                if len(full_number)%2 != 0: #if the entire string is an odd length, true double ups don't exist
                    continue
                # all examples are double around the mid point, this also prevents double ups (e.g. 8x1 and 4x2 in a 22222222 ID)
                mid = len(full_number) //2
                if full_number[:mid] == full_number[mid:]:
                    print(full_number)
                    code += int(full_number)
                
    print(code)
                                 
                                 
                                
                

