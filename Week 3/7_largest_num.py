import sys

def largest_number(a,n):
    res = ""
    while(a):
        maxi=a[0]
        maxindex=0
        for i,each in enumerate(a):
            if IsGreaterOrEqual(each,maxi):
                maxi=each
                maxindex=i
        res += maxi
        del a[maxindex]
    return res

def IsGreaterOrEqual(A,B):
    return int(A+B)>int(B+A)

if __name__ == '__main__':
    data = sys.stdin.read().split()
    n=int(data[0])
    a = data[1:]
    print(largest_number(a,n))