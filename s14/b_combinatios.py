key = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def recursion(dictionary, digits, idx, res, result):
    if idx >= len(digits):
        result.append(res)
        return

    for c in dictionary[digits[idx]]:
        recursion(dictionary, digits, idx + 1, res + c, result)


if __name__ == "__main__":
    input = input()
    result = []
    recursion(key, input, 0, '', result)
    print(*result)
