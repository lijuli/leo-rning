import sys


first_line = str(sys.stdin.readline().rstrip())
second_line = str(sys.stdin.readline().rstrip())
extra = None

for char in second_line:
    if char not in first_line:
        print(char)
    if 1 < second_line.count(char) > first_line.count(char):
        extra = char
if extra is not None:
    print(extra)
