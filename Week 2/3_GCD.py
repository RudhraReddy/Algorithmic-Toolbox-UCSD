def gcd_x(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd_x(b,a%b)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_x(a, b))