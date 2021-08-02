def bubble_sort(arr):

    for outer_idx in range(len(arr)):
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[1+i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            if outer_idx == 0:
                print(*arr)
            return
        else:
            print(*arr)


if __name__ == "__main__":
    length_arr = input()
    input_arr = [int(x) for x in input().split()]

    bubble_sort(input_arr)
