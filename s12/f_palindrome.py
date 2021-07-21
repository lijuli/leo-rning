import sys

line = sys.stdin.readline().rstrip()
line = ''.join(e for e in line if e.isalnum()).lower()


def is_palindromic(string):
    for i in range(len(string)//2):
        if not string[i] == string[-i-1]:
            return False
    return True


print(is_palindromic(line))
