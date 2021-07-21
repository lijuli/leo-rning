
number = int(input())
r = 1
binary = ''

while True:
    r = number % 2
    if r == 0:
        binary += '0'
    if r > 0:
        binary += '1'
    number = number//2
    if number == 0:
        break

print(binary[::-1])
