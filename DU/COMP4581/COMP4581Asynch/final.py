

def f(n):
    j = 0
    for i in range(-2*n, 2*n):
        print('Loop')
        j+=1
    return j

stuff = f(3)
print(stuff)