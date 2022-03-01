"""
Ben Karabinus
University of Denver
COMP 4581, Winter 2022
Lab 8
"""


def printMatrix(m):
    for row in m:
        print(row)


def parenStr(traceback, start, stop):

    """could not figure out how to remove the extra parenthesis on each end.
       Possible different choice: use data structure indtead of printing recursively
    """
    # base case
    if start == stop:
        print("(A{})".format(start), end="")
    else:
        print("(", end='')
        parenStr(traceback, start, traceback[start][stop])
        parenStr(traceback, traceback[start][stop] + 1, stop)
        print(")", end='')


def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims)-1
    m = [[None for i in range(n)] for j in range(n)]
    # create the taceback table
    traceback = [[None for i in range(n)]for j in range(n)]
    # Fill in the base case values
    for i in range(n):
        m[i][i] = 0
    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2,n+1): 
        for i in range(n+1-chainLength):
            j = i + chainLength - 1
        # Fill in m[i][j] with the best of the recursive options
            m[i][j] = float("inf")
            for k in range(i, j):
        # Two previous table values plus
        # what it cost to mult the resulting matrices
                q = m[i][k]+m[k+1][j]+dims[i]*dims[k+1]*dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    # add indicies of best paren to traceback table
                    traceback[i][j] = k

    parenStr(traceback, 0, n-1)
    print()
    return m[0][n-1]


def main():
    dims = [30, 35, 15, 5, 10, 20, 25]
    print(chainMatrix(dims))


if __name__ == '__main__':
    main()
