import string
import sys

filename = sys.argv[1] # dis is filename
grid = []

try:
    numfile = open(filename)

except:
    exit()

try:
    for line in numfile:
        grid += [string.split(line)]
    
    numfile.close()

except:
    exit()

#following converts grid into list of list of ints (instead of string)
for line in range(0, len(grid)):
    for num in range(0, len(grid[line])):
        grid[line][num] = int(grid[line][num])

l_prod = 1 #will end up being largest product

#start of horizontal products
s_col = 0
e_col = 4 # these are the indexes for rows

for row in grid:
    while e_col <= len(row):
        temp_prod = 1

        for num in row[s_col:e_col]:
            temp_prod *= num
        
        if temp_prod > l_prod:
            l_prod = temp_prod
                    
        s_col += 1
        e_col += 1

    s_col = 0
    e_col = 4    
#end of horizontal products
#print l_prod

#start of column products
#takes 4 rows at a time
#moves left to right a column at a time
col_idx = 0
s_row = 0
e_row = 4

while e_row <= len(grid):
    while col_idx < len(grid[0]):
        temp_prod = 1

        for row in grid[s_row:e_row]:
            temp_prod *= row[col_idx]
            
        if temp_prod > l_prod:
            l_prod = temp_prod
        
        col_idx += 1

    if col_idx == len(grid[0]):
        col_idx = 0
        s_row += 1
        e_row += 1
#end of column products
#print l_prod

#start of diagonal topleft-bottomright
#takes 4 rows at a time
#moves left-right diagonally
s_row = 0
e_row = 4
s_col = 0
e_col = 4

while e_row <= len(grid):
    while e_col <= len(grid[0]):
        temp_grid = grid[s_row:e_row] #4 rows at a time
        temp_prod = 1
        diag_nums = range(s_col, e_col)
        idx = 0

        while idx < 4:
            temp_prod *= temp_grid[idx][diag_nums[idx]]
            #print temp_grid[idx][diag_nums[idx]]
            idx += 1
 
        idx = 0

        if temp_prod > l_prod:
            l_prod = temp_prod

        s_col += 1
        e_col += 1

    s_col = 0
    e_col = 4
    s_row += 1
    e_row += 1
#end of diagonal topleft-bottomright

#start of diagonal topright-bottomleft
#takes 4 rows at a time
#moves left-right along rows, however diagonal is bottomleft-topright
s_row = 0
e_row = 4
s_col = 0
e_col = 4

while e_row <= len(grid):
    while e_col <= len(grid[0]):
        temp_grid = grid[s_row:e_row]
        temp_prod = 1
        diag_nums = range(e_col - 1, s_col - 1, -1)
        idx = 0

        while idx < 4:
            temp_prod *= temp_grid[idx][diag_nums[idx]]
            #print temp_grid[idx][diag_nums[idx]]
            idx += 1

        idx = 0

        if temp_prod > l_prod:
            l_prod = temp_prod

        s_col += 1
        e_col += 1

    s_col = 0
    e_col = 4
    s_row += 1
    e_row += 1

print l_prod
