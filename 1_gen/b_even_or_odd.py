# «WIN» or «FAIL»

# input
# 1 2 -3
# FAIL

# input
# 7 11 7
# WIN

# input
# 6 -2 0
# WIN

# line = sys.stdin.readline().rstrip()
# line = input()


def is_even(number):
    return number % 2 == 0


triplets = [int(x) for x in input().split()]


def get_result(triplets):
    flag = is_even(triplets[0])

    for i in range(1, len(triplets)):
        if flag != is_even(triplets[i]):
            return 'FAIL'
    return 'WIN'


print(get_result(triplets=triplets))

# if (is_even(a) + is_even(b) + is_even(c)) in (0, 3):
#     print('WIN')
# else:
#     print('FAIL')
