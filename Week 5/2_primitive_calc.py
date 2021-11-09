# Uses python3
import sys
import numpy
def optimal_sequence(n):
    min_ca=numpy.zeros((n+1),dtype=int)
    for each in range(2,n+1):
        listt=[]
        if each%3==0:
            listt.append(min_ca[each//3]+1)
        if each%2==0:
            listt.append(min_ca[each//2]+1)
        listt.append(min_ca[each-1]+1)
        min_ca[each]=min(listt)
    return min_ca
def OutputAlignment(n,min_ca):
    if n==1:
        print(1,end=' ')
        return
    if n%3==0 and min_ca[n]==min_ca[n//3]+1:
        OutputAlignment(n//3,min_ca)
        print(n,end=' ')
    elif n%2==0 and min_ca[n]==min_ca[n//2]+1:
        OutputAlignment(n//2,min_ca)
        print(n,end=' ')
    else:
        OutputAlignment(n-1,min_ca)
        print(n,end=' ')
input = sys.stdin.read()
x = int(input)
y =optimal_sequence(x)
print(y[x])
OutputAlignment(x,y)