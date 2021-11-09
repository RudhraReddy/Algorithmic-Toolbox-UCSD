import sys
def max_dot_product(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    a.sort()
    b.sort()
    print(max_dot_product(a, b))