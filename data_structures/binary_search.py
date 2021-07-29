def binary_search1(arr, left, right, x):
    if right >= left:
        mid = (left + right) // 2

        if arr[mid] >= x:
            return mid
        elif arr[mid] > x:
            return binary_search1(arr, left, mid, x)
        else:
            return binary_search1(arr, mid + 1, right, x)
    else:
        return -1


if __name__ == "__main__":
    arr = [1, 4, 4, 4, 6, 8]
    x = 3

    result = binary_search1(arr, 0, len(arr)-1, x)
    print(result)
    result2 = binary_search1(arr, result+1, len(arr)-1, x*2)
    print(result2)