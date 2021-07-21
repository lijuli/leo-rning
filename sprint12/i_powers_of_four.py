number = int(input())

while True:
    if number == 1:
        print(True)
        break
    if number % 4 != 0:
        print(False)
        break
    number = number / 4
    # if number == 1:
    #     flag = True
    #     break

# print(flag)
