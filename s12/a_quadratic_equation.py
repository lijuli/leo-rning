# input a, x, b, c.
# output f(x)

# input: -8 -5 -2 7  output: -183
# input: 8 2 9 -10  output: 40


a, x, b, c = map(int, input().split())
y = a*x*x + b*x + c
print(y)
