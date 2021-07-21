first_number = str(input())
second_number = str(input())
third_number = ''


def add(a, b):
    result = ''
    if a == '0':
        if a == b:
            result = result + '0'
        result = result + '1'
    if a == '1':
        if a == b:
            result = result + '10'
        result = result + '1'
    return result


for f_char, s_char in zip(first_number[::-1], second_number[::-1]):
    third_number += add(f_char, s_char)

print(third_number[::-1])
