# https://contest.yandex.ru/contest/22450/run-report/64840624/

def find_closest_zero(n, sequence):
    last_zero_idx = None
    distances = [float('inf')]*n

    for current_idx in range(n):
        if sequence[current_idx] == '0':
            last_zero_idx = current_idx
            distances[current_idx] = 0
        elif last_zero_idx is not None:
            distances[current_idx] = current_idx - last_zero_idx

    for current_idx in range(last_zero_idx + 1)[::-1]:
        if sequence[current_idx] == '0':
            last_zero_idx = current_idx
        if (distances[current_idx] is float('inf')
                or distances[current_idx] > last_zero_idx - current_idx):
            distances[current_idx] = last_zero_idx - current_idx

    return distances


if __name__ == "__main__":
    total_houses = int(input())
    houses = list(input().split())

    print(*find_closest_zero(total_houses, houses))
