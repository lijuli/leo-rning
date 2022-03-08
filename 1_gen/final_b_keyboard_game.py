MATRIX_SIZE = 4
KEY_NUMBERS = '123456789'


def find_max_score(keys, k):
    return sum([0 < keys.count(key) <= k for key in KEY_NUMBERS])


if __name__ == "__main__":
    k = int(input())*2
    key_input = ''
    for column in range(MATRIX_SIZE + 1):
        try:
            key_input += input()
        except EOFError:
            break

print(find_max_score(key_input, k))
