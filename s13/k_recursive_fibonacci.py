def get_fibonacci(n):
    if n == 1 or n == 0:
        return 1
    a = 1
    b = 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b


if __name__ == "__main__":
    number, k = map(int, input().split())
    fibonacci = get_fibonacci(number)
    r = fibonacci % 10**k
    print(r)
