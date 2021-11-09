def gcd_x(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd_x(b,a%b)

def lcm_y(a,b):
    return (a*b)//gcd_x(a,b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_y(a, b))