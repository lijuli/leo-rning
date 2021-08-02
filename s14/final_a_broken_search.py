def binary_search(arr, left, right, x):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == x:
        return mid

    if arr[left] < arr[mid]:
        if arr[left] <= x < arr[mid]:
            return binary_search(arr, left, mid - 1, x)
        return binary_search(arr, mid + 1, right, x)
    else:
        if arr[mid] < x <= arr[right]:
            return binary_search(arr, mid + 1, right, x)
        return binary_search(arr, left, mid - 1, x)


def broken_search(nums, target) -> int:
    return binary_search(nums, 0, len(nums) - 1, target)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    assert broken_search(arr, 19) == 0
    assert broken_search(arr, 21) == 1
    assert broken_search(arr, 101) == 3
    assert broken_search(arr, 1) == 4
    assert broken_search(arr, 4) == 5
    assert broken_search(arr, 12) == 8
    assert broken_search(arr, 8) == -1
