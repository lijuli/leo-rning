def find_closest_zero(n, sequence):
    last_zero_idx = None
    distances = [None]*n

    for current_idx in range(n):
        if sequence[current_idx] == '0':
            last_zero_idx = current_idx
            distances[current_idx] = 0
        elif last_zero_idx is not None:
            distances[current_idx] = current_idx - last_zero_idx

    for current_idx in range(last_zero_idx + 1)[::-1]:
        if sequence[current_idx] == '0':
            last_zero_idx = current_idx
        if (distances[current_idx] is None
                or distances[current_idx] > last_zero_idx - current_idx):
            distances[current_idx] = last_zero_idx - current_idx

    return distances


if __name__ == "__main__":
    total_houses = int(input())
    houses = [x for x in input().split()]
    #
    # total_houses = 5
    # houses = ['0', '1', '4', '9', '0']

    # total_houses = 6
    # houses = [0, 7, 9, 4, 8, 20]

    # total_houses = 7
    # houses = [0, 7, 9, 4, 0, 0, 20]  # 0 1 2 1 0 1

    # total_houses = 5
    # houses = ['1', '2', '5', '0', '4']  # 3 2 1 0 1

    print(*find_closest_zero(total_houses, houses))
    # print(*find_closest_zeroes(total_houses, houses))
