import sys

text_length = 19 #int(input())
word = ''
length = 0


for i in range(text_length):
    char = sys.stdin.read(1)
    print(f'i={i}')
    if char != ' ':
        word = word + char
        length += 1
    if char == ' ':
        print(word)
        print(length)
        word = 0
        length = 0


