import sys

def merge(a, b, left, ave, right):
    i, j, k = left, ave, left
    count = 0
    while (i <= ave -1 and j <= right):
        if (a[i] <= a[j]):
            b[k] = a[i]
            i += 1
            k += 1
        else:
            b[k] = a[j]
            count += ave - i
            j += 1
            k += 1
    while (i <= ave - 1):
        b[k] = a[i]
        i += 1
        k += 1
    while (j <= right):
        b[k] = a[j]
        j += 1
        k += 1
    for i in range(left,right+1):
        a[i] = b[i]
    return count

def num_inversions(a, b, left, right):
    inversions = 0
    if right <= left:
        return inversions
    ave = (left + right) // 2
    inversions += num_inversions(a, b, left, ave)
    inversions += num_inversions(a, b, ave+1, right)
    inversions += merge(a, b, left, ave+1, right)
    return inversions

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, sys.stdin.read().split()))
    b = n * [0]
    print(num_inversions(a, b, 0, len(a)-1))