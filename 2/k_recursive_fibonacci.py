def get_fibonacci(n, k):
    m = 10**k
    if n == 1 or n == 0:
        return 1
    a = 1
    b = 1
    res = 0
    for _ in range(2, n+1):
        a, b = b, a+b
        res = b % m
    return res


if __name__ == "__main__":
    number, k = map(int, input().split())
    print(get_fibonacci(number, k))
