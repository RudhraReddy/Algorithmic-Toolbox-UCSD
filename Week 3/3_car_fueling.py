import sys

def compute_min_refills(distance, tank, stops):
    stops.append(distance)
    last_refill=0
    dist=0
    num=0
    i=-1
    while(dist<distance):
        while(dist<distance and last_refill+tank>=stops[i+1] ):
            i+=1
            dist=stops[i]
        if dist==last_refill:
            return -1
        num+=1
        last_refill=dist
    num-=1
    return num

if __name__ == '__main__':
    x, y, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(x, y, stops))