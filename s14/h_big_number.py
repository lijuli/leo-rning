def compare_first_digit(number1, number2):
    temp1 = number1 + number2
    temp2 = number2 + number1
    return temp1 > temp2


def insertion_sort(arr):
    for i in range(len(arr)):
        insert = arr[i]
        j = i

        while j > 0 and compare_first_digit(insert, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1

        arr[j] = insert


def find_biggest_number(arr):
    insertion_sort(arr)
    s = ''
    for item in arr:
        s += item
    return s


if __name__ == "__main__":
    length_arr = input()
    input_arr = [x for x in input().split()]

    result = find_biggest_number(input_arr)
    print(result)



