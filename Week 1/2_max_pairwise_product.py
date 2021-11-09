# max pairwise product
def max_pairwise_fast(a):
    n=len(a)
    p=0
    q=0
    for f in range(n):
        if p<a[f]:
            p=a[f]
            max_index=f
    for s in range(n):
        if q<a[s] and s!=max_index:
            q=a[s]
    return p*q

if __name__ == '__main__':
    x = int(input())
    y = [int(i) for i in input().split()]
    print(max_pairwise_fast(y))
