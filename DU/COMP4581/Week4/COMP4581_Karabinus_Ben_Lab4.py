"""
Ben Karabinus
University of Denver
COMP 4581 Winter Quarter 2022
Lab 4
"""


def main():

    A = [7, 4, 12, 14, 2, 10, 16, 6]
    B = [7, 4, 12, 14, 2, 10, 16, 5]
    C = [14, 8, 2, 6, 3, 10, 12]
    print("A: ", A)
    print("B: ", B)
    print("C: ", C)
    aDist = recCPairDistPoints(mergeSort(A))
    bDist = recCPairDistPoints(mergeSort(B))
    cDist = recCPairDistPoints(mergeSort(C))
    print("The minimum distance between any two points in A is ", aDist)
    print("The minimum distance between any two points in B is ", bDist)
    print("The minimum sistance between any two points in C is ", cDist)


# function for merge sort
def mergeSort(L):  # log_2(n)
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        Left = mergeSort(L[:mid])
        Right = mergeSort(L[mid:])
        return merge(Left, Right)


# function to merge sorted sublists
def merge(A, B):
    out = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            out.append(A[i])
            i += 1
        else:
            out.append(B[j])
            j += 1
    while i < len(A):
        out.append(A[i])
        i += 1
    while j < len(B):
        out.append(B[j])
        j += 1
    return out


# find the distance between points in a list, 1-D, len(list)<=3
def cPairDist(points):
    minD = abs(points[0]-points[1])
    if len(points) == 2:
        return minD
    d = abs(points[1] - points[2])
    if minD > d:
        return d
    d = abs(points[0]-points[2])
    if minD > d:
        return d

    return minD


# recusrsiv function to find distance between two points
def recCPairDistPoints(points):
    mid = len(points)//2
    # base case
    if len(points) < 2:
        return float('inf')
    if len(points) <= 3:
        return cPairDist(points)
    # divide
    left = points[:mid]
    right = points[mid+1:]
    # conquer
    minLeft = recCPairDistPoints(left)
    minRight = recCPairDistPoints(right)
    # combine
    minCross = cPairDist([points[mid-1], points[mid], points[mid+1]])
    minD = min(minLeft, minRight, minCross)

    return minD


if __name__ == '__main__':
    main()
