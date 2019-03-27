#40!/(20!20!)
#following code is not finished... nor is it the method used to solve

def lattice_paths(num): 
    '''takes n of square grid and returns max number of moves'''
    poss_moves = [] #list of 1's and 0's that represent moves
    #each move is a permutation of above list
    count = 1

    for move in range(0, num):
        poss_moves += [1] #1 represents right
    
    for move in range(0, num):
        poss_moves += [0] #0 represents down

    
    return poss_moves

print lattice_paths(2)

print lattice_paths(3)
