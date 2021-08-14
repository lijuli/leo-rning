import time

def binary_search(array, item, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    # print(item, array[mid])
    if item == array[mid]:
        return mid
    if item > array[mid]:
        return binary_search(array, item, mid+1, end)
    return binary_search(array, item, start, mid-1)

def search(array, item, mid=None, left=None, right=None):
    left = array[0]
    right = array[-1]
    mid_item = array[mid]
    length = len(array)
    if left == item or right == item or mid_item == item:
        return array.index(item)
    if left < mid_item:
        if left < item < mid_item:
            return binary_search(array, item, 0, mid+1)
        if left > item < mid_item:
            return search(array, item, mid+1)
        if item > mid_item:
            return binary_search(array, item, mid, length-1)
    if left > mid_item:
        if item > mid_item:
            return binary_search(array, item, mid, length-1)
        if item < mid_item:
            return binary_search(array, item, 0, mid+1)
    return -1


def broken_search(nums, target) -> int:
    mid = len(nums) // 2
    return search(nums, target, mid)


if __name__ == "__main__":
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    t = time.time()
    broken_search(arr, 5)
    # print(n)
    print("Function call: " + str(time.time() - t))
    # dis.dis(solution)
