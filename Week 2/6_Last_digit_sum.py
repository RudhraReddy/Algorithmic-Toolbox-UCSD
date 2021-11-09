def sum_last_digit(n):
    if n <= 1:
        return n
    p = 0
    q  = 1
    for _ in range(n - 1):
        p, q = q, (1+p + q)%10
    return q

def pisano_period(m):
    p=0
    q=1
    for i in range(m*m):
        p, q = q, (p + q)%m
        if p==0 and q==1:
            return (i+1)

if __name__ == '__main__':
    x=pisano_period(10)
    y=sum_last_digit(x)
    n = int(input())
    print((sum_last_digit(n%x)+(y*(n//x))%10)%10)