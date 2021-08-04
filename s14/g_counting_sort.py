def collect(counted, arr):
    idx = 0
    for i in range(3):
        for _ in range(counted[i]):
            arr[idx] = i
            idx += 1


def counting_sort(arr, n):
    counted = [
        arr.count('0'),
        arr.count('1'),
        arr.count('2')
    ]

    idx = 0
    for i in range(3):
        for _ in range(counted[i]):
            arr[idx] = i
            idx += 1

    return arr


if __name__ == "__main__":
    n = int(input())
    k = 3
    arr = [x for x in input().split()]
    res = counting_sort(arr, n)
    print(*res)
