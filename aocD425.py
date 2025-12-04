import numpy as np

def check(i, j, grid):
    count = 0
    for row in range(i-1, i+2):
        for col in range(j-1,j+2):
            print(row, col)
            if row < 0 or col <0 :
                continue#print("Out of the grid Top, Left")
            elif row >= np.shape(grid)[0] or col >= np.shape(grid)[1]:
                print("Out of the grid Bottom, Right")
                print(np.shape(grid)[0], np.shape(grid)[1])
            else:
                if grid[row][col] == '@': 
                    #print("@ found", grid[row][col])
                    count+=1
                else:
                    #print("@ not found", grid[row][col])
                    continue
    return count   
    


with open("testD4.txt", "r") as file:
    g = file.read().strip() #strip the file of any unwanted guests
    lines = int(g.count('\n') +1) #how many lines
    allg = list(g.replace('\n', ''))
    length = int(len(allg)/lines) #how many per line
    grid = np.array(allg).reshape(lines, length) #put into array
    viable_places = 0
    print(np.shape(grid)[0], np.shape(grid)[1])
    for i in range(0, lines):
        for j in range(0, length):
            if grid[i][j] == '@':
                print("Toilet Paper here")
                count = check(i, j, grid)
                if count <= 4:
                    print("Viable")
                    viable_places += 1
            else:
                print("No Toilet Paper Here")
    print(viable_places)


                
