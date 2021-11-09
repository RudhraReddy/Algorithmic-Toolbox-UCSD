def get_change(y):
    count=0
    while(y>0):
        if y>=10:
            y=y-10
        elif y>=5:
            y-=5
        elif y>=1:
            y-=1
        count+=1
    return count

if __name__ == '__main__':
    x = int(input())
    print(get_change(x))