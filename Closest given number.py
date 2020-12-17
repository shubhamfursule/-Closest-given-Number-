from random import randint

def closest(L,n):
    L.sort()
    max1=L[0]
    for i in range(1,len(L)):
        if L[i]<n and max1<n:
            max1=L[i]
    return max1
        
L1=[randint(0,30) for i in range(int(8))]
print(L1)
n1=int(input("Please Enter number that you want to get the closest number:  "))
print(f"\"{closest(L1,n1)}\" is the Closest number of {n1}" )
