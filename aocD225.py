"""
To extract the Data into aoc.txt Steps in obsidian
"""
bruh = 0


with open("testD2.txt", "r") as file:
    allcode = file.read() # Read file
    all_IDs = allcode.split(',')
    all_invalid_IDS = []
    for id in all_IDs:
        first_ID = int(id.split('-')[0])
        last_ID = int(id.split('-')[1])
        full_ID = list(range(first_ID, (last_ID+1)))
        all_invalid_ID = []
        print(full_ID)