import sys
import numpy

def get_change(m):
    mincoins=numpy.zeros((m+1),dtype=int)
    for x in range(1,m+1):
        listt=[]
        for y in [1,3,4]:
            if x>=y:
                listt.append(mincoins[x-y]+1)
        mincoins[x]=min(listt)
    return mincoins[m]



if __name__ == '__main__':
    a = int(sys.stdin.read())
    print(get_change(a))