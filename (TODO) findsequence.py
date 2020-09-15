import numpy as np

'''def checkio(matrix):
    # Alter dimensions as needed
    # create a default array of specified dimensions
    a = np.array(matrix)
    
    x,y = a.shape[1],a.shape[0]

    # a.diagonal returns the top-left-to-lower-right diagonal "i"
    # according to this diagram:
    #
    #  0  1  2  3  4 ...
    # -1  0  1  2  3
    # -2 -1  0  1  2
    # -3 -2 -1  0  1
    #  :
    #
    # You wanted lower-left-to-upper-right and upper-left-to-lower-right diagonals.
    #
    # The syntax a[slice,slice] returns a new array with elements from the sliced ranges,
    # where "slice" is Python's [start[:stop[:step]] format.

    # "::-1" returns the rows in reverse. ":" returns the columns as is,
    # effectively vertically mirroring the original array so the wanted diagonals are
    # lower-right-to-uppper-left.
    #
    # Then a list comprehension is used to collect all the diagonals.  The range
    # is -x+1 to y (exclusive of y), so for a matrix like the example above
    # (x,y) = (4,5) = -3 to 4.
    diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]

    # Now back to the original array to get the upper-left-to-lower-right diagonals,
    # starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
    diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

    #add rows and columns to diags:
    diags.extend(a[i] for i in range(a.shape[1]))
    diags.extend(a[:, i] for i in range(a.shape[0]))
    
    #listofthings = [n.tolist() for n in diags]
    listofthings = [[1,1,1,1]]
    #check for repeat patterns
    for i in listofthings:
        if len(i) > 3:
            for j in range(0, len(i)-4):
                print(j)
                print(i[j])
                print(i[j:j+3])
                if i[j:j+3].count(i[j]) == 4:
                    return True
        
    return False


checkio([[1,2,1,1],[1,1,4,1],[1,3,1,6],[1,7,2,5]])
'''
i = [1,1,1,1]
if len(i) > 3:
    for j in range(0, len(i)-4):
        print(j)
        print(i[j])
        print(i[j:j+3])
        if i[j:j+3].count(i[j]) == 4:
            print("True")
else:
    print("False")