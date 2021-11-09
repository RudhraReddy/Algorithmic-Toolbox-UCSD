def optimal_summands(x):
    arr = []
    var=1
    while(True):
        if (x>=2*var+1):
            arr.append(var)
        else:
            arr.append(x)
            break
        x-=var
        var+=1
    return arr

if __name__ == '__main__':
    arr = optimal_summands(int(input()))
    print(len(arr))
    for i in arr:
        print(i, end=' ')