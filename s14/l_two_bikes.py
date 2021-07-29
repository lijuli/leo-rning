def binary_search1(arr, left, right, x):
    if arr[len(arr)-1] < x:
        return -1

    if x <= arr[0]:
        return 1

    if right < left:
        return -1

    mid = (left + right) // 2

    if mid == 0:
        if arr[mid] <= x:
            return mid + 1

    if x <= arr[mid]:
        if arr[mid-1] < x:
            return mid + 1
        return binary_search1(arr, left, mid, x)
    return binary_search1(arr, mid + 1, right, x)


if __name__ == "__main__":
    length = int(input())
    arr = [int(x) for x in input().split()]
    x = int(input())

    brother_idx = binary_search1(arr, 0, length - 1, x)
    if brother_idx == -1:
        sister_idx = -1
    else:
        sister_idx = binary_search1(arr, brother_idx, length - 1, x*2)

    print(brother_idx, sister_idx)
