def sum_of_two_digits(x, y):
    return x + y

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
