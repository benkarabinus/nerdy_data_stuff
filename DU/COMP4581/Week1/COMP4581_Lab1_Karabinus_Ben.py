'''
Ben Karabinus
COMP 4581 Winter 2022
Lab 1

'''

# function to print matrices
def printMatrix(m):
    for row in m:
        print(row)


# function to create empty matrix
def createEmptyMat(rows, columns):
    emptyMat = [[None for i in range(columns)]for j in range(rows)]
    return emptyMat


# function to multiply two matrices
def matrixMult(A,B):
    colsA = len(A[0])
    rowsA = len(A)
    colsB = len(B[0])
    rowsB = len(B)
    C = None
    if colsA == rowsB:
        C = createEmptyMat(rowsA, colsB)
        for i in range(0, rowsA):
            for j in range(0, colsB):
                sum = 0
                for k in range(0, colsA):
                    sum += A[i][k]*B[k][j]
                C[i][j] = sum
    return C


# Testing code
# Test1
A = [[ 2, -3, 3],
[-2, 6, 5],
[ 4, 7, 8]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7]]
C = matrixMult(A, B) 
if not C == None:
    printMatrix(C)

# Test2
A = [[ 2, -3, 3, 0],
[-2, 6, 5, 1],
[ 4, 7, 8, 2]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7]]
C = matrixMult(A, B) 
if not C == None:
    printMatrix(C)
else:
    print("The product of the two matrices is not defined.")

# Test3
A = [[ 2, -3, 3, 5],
[-2, 6, 5, -2]]
B = [[-1, 9, 1],
[ 0, 6, 5],
[ 3, 4, 7],
[ 1, 2, 3]]
C = matrixMult(A, B) 
if not C == None:
    printMatrix(C)

