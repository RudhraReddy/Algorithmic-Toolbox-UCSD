def last_digit(n):
    if n <= 1:
        return n

    p = 0
    q  = 1

    for _ in range(n - 1):
        p, q = q, (p + q)%10

    return q

if __name__ == '__main__':
    x = int(input())
    print(last_digit(x))