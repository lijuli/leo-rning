def in_place_quicksort(array):
    def quicksort_step(left, right):
        def partition(left, right):
            pivot = left
            for current in range(left + 1, right + 1):
                if array[current] < array[left]:
                    pivot += 1
                    array[current], array[pivot] = array[pivot], array[current]
            array[pivot], array[left] = array[left], array[pivot]
            return pivot
        if right - left < 1:
            return
        pivot = partition(left, right)
        quicksort_step(left, pivot-1)
        quicksort_step(pivot+1, right)
    quicksort_step(0, len(array)-1)
    return array

if __name__ == '__main__':
    print(
        *(login for _, _, login in in_place_quicksort([
            (lambda login, score, penalty: [-int(score), int(penalty), login])(
                *input().split()
            )
            for _ in range(int(input()))
        ])),
        sep='\n'
    )
