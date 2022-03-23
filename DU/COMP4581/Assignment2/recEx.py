import random

def binSearch(L, target):
    print(L)

    #base
    if len(L) == 0:
        return False

    #rec
    else:
        mid = len(L)//2
        if L[mid] == target:
            return True
        elif L[mid] > target:
            low = L[:mid]
            return binSearch(low, target)
        else:
            high = L[mid+1:]
            return binSearch(high, target)


def listMax(L):
    #base
    if len(L) == 1:
        return L[0]
        
    #rec
    else:
        mid = len(L)//2
        left = L[:mid]
        right = L[mid:]
        lmax = listMax(left)
        rmax = listMax(right)
        return max(lmax, rmax)


def expon(a, b):
    print(b)
    
    #base
    if b==0:
        return 1
    
    #rec
    else:
        if (b%2 == 0):
            x = expon(a, b//2)
            return x * x
        else:
            return a * expon(a, b-1)

print(expon(2, 53))
    
#a = [i for i in range(10)]
#print(binSearch(a, 15))

#random.shuffle(a)
#print(a)
#print(listMax(a))

