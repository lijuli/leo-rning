def compare(a, b):
    return [a[1], -a[2], b[0]] < [b[1], -b[2], a[0]]


def for_partition(arr, left, right):
    pivot = arr[right]
    for i in range(left, right):
        if compare(pivot, arr[i]):
            arr[i], arr[left] = arr[left], arr[i]
            left += 1

    arr[left], arr[right] = arr[right], arr[left]
    return left


def quick_sort(arr, left, right):
    if len(arr) == 1:
        return
    if left < right:
        partition = for_partition(arr, left, right)

        quick_sort(arr, left, partition - 1)

        quick_sort(arr, partition + 1, right)


if __name__ == "__main__":
    competitors = []
    n = int(input())
    for _ in range(n):
        inp = input().split()
        inp[1] = int(inp[1])
        inp[2] = int(inp[2])

        competitors.append(
            [x for x in inp]
        )

    quick_sort(competitors, 0, n - 1)
    for competitor in competitors:
        print(competitor[0])