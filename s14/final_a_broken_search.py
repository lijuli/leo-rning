def binary_search(arr: list, left: int, right: int, target: int) -> int:
    """Implements binary search in sorted and rotated list of numbers."""
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if arr[left] < arr[mid]:
        if arr[left] <= target < arr[mid]:
            return binary_search(arr, left, mid - 1, target)
        return binary_search(arr, mid + 1, right, target)
    else:
        if arr[mid] < target <= arr[right]:
            return binary_search(arr, mid + 1, right, target)
        return binary_search(arr, left, mid - 1, target)


def broken_search(nums: list, target: int) -> int:
    """
    Returns target index in given list.

    Args:
        nums: A list of integers.
        target: A target element that should be found in mums list. An integer.

    Returns:
        Index of target element. Returned item is integer.
        If the target element cannot be found - returns -1.
    """
    return binary_search(nums, 0, len(nums) - 1, target)
