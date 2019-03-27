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

x = 0
y = 0
horizontal = 0
vertical = 0
diag_dr = 0
diag_ur = 0
l_prod = 1

for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if x <= len(grid[0]) - 4:
            horizontal = grid[y][x] * grid[y][x+1] * grid[y][x+2] * grid[y][x+3]
            
            if horizontal > l_prod:
                l_prod = horizontal

        if y <= len(grid) - 4:
            vertical = grid[y][x] * grid[y+1][x] * grid[y+2][x] * grid[y+3][x]

            if vertical > l_prod:
                l_prod = vertical

        if x <= (len(grid[0]) -4) and y <= (len(grid) - 4):
            diag_dr = grid[y][x] * grid[y+1][x+1] * grid[y+2][x+2] * grid[y+3][x+3]

            if diag_dr > l_prod:
                l_prod = diag_dr
        
        if x >= 3 and y <= (len(grid) - 4):
            diag_ur = grid[y][x] * grid[y+1][x-1] * grid[y+2][x-2] * grid[y+3][x-3]

            if diag_ur > l_prod:
                l_prod = diag_ur

print l_prod
