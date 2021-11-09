def fibonacci_mod(n,m):
    if n <= 1:
        return n
    p = 0
    q  = 1
    for _ in range(n - 1):
        p, q = q, (p + q)%m
    return q

def fibonacci_huge(n,m):
    return fibonacci_mod(n%(pisano_period(m)),m)

def pisano_period(m):
    p=0
    q=1
    for i in range(m*m):
        p, q = q, (p + q)%m
        if p==0 and q==1:
            return (i+1)

if __name__ == '__main__':
    n = int(input())
    print((fibonacci_huge(n, 10)*fibonacci_huge(n+1, 10))%10)