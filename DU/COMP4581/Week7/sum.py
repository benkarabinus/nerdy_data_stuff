
import math
def getMinSquaresDAC(n):

    # base
    if n==0:
        return 0

    else: # rec
        result = n+1

        stopSquare = math.floor(math.sqrt(n))+1
        
        for i in range(1, stopSquare):
            currentSq = i*i

            currentResult = 1 + getMinSquaresDAC(n - currentSq)
            
            result = min(result, currentResult)

        return result


def getMinSquaresDP(n):

    minSq = [None for i in range(n+1)]

    # base
    minSq[0] = 0

    for tableIndex in range(1, n+1):
        print(minSq)

        stopSquare = math.floor(math.sqrt(tableIndex))+1
        result = tableIndex+1
        for i in range(1, stopSquare):
            currentSq = i*i

            currentResult = 1 + minSq[tableIndex - currentSq]
            
            result = min(result, currentResult)

        minSq[tableIndex] = result

    print(minSq)
    return minSq[n]

            
print(getMinSquaresDAC(10))
print(getMinSquaresDP(10))
