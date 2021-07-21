# https://contest.yandex.ru/contest/23390/run-report/52101870/
MATRIX_SIZE = 4


def read_pressed_keys():
    keys = {}
    for column in range(MATRIX_SIZE + 1):
        try:
            for key in input():
                if key == '.':
                    continue
                if key not in keys:
                    keys[key] = 1
                    continue
                keys[key] += 1
        except EOFError:
            break
    return keys


def find_max_score(keys, max_keys_pressed):
    total_keys_pressed = max_keys_pressed * 2
    score = 0
    # score = sum[ count(value) for value in keys.values()]
    for value in keys.values():
        if value <= total_keys_pressed:
            score += 1
    return score


if __name__ == "__main__":
    k = int(input())
    keys_pressed = read_pressed_keys()
    max_score = find_max_score(keys_pressed, k)
    print(max_score)