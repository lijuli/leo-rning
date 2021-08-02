def compare(a, b):
    # Returns true if a > b
    return [-a[1], a[2], a[0]] < [-b[1], b[2], b[0]]


def partition(arr, pivot):
    left = []
    center = []
    right = []
    for i in arr:
        if i < pivot:
            left.append(i)

        if i > pivot:
            right.append(i)

        if i == pivot:
            center.append(i)

    return left, center, right


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left, center, right = partition(arr, pivot)
        return quick_sort(left) + center + quick_sort(right)


if __name__ == "__main__":
    arr = [
        ['alla', 4, 100],
        ['gena', 6, 1000],
        ['gosha', 2, 90],
        ['rita', 2, 90],
        ['timofey', 4, 80]
    ]

    arr2 = [
        ['alla', 0, 0],
        ['gena', 0, 0],
        ['gosha', 0, 0],
        ['rita', 0, 0],
        ['timofey', 0, 0]
    ]

    alla = arr[0]
    gena = arr[1]

    # print(compare(arr[0], arr[1]))

    nums = [5, 7, 4, 3, 6]
    n = quick_sort(nums)
    print(n)
