# input: x y
# output: the product of x*y

def multiply(x, y):
    x_s = str(x)
    y_s = str(y)

    n = max(len(x_s), len(y_s))
    n2 = n//2

    if len(x_s) == 1 or len(y_s) == 1:
        return x * y

    a = x // 10 ** n2
    b = x % 10 ** n2
    c = y // 10 ** n2
    d = y % 10 ** n2

    p = a + b
    q = c + d

    ac = multiply(a, c)
    bd = multiply(b, d)
    pq = multiply(p, q)
    adbc = pq - ac - bd

    result = (10**(2*n2)) * ac + (10**n2) * adbc + bd
    return result


print(multiply(5678, 1234))
