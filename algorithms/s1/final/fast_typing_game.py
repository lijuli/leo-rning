# https://contest.yandex.ru/contest/22450/run-report/64841790/

BOARD_SIZE = 4
ALL_KEYS = '123456789'


def read_input():
    keys = {}
    for column in range(BOARD_SIZE + 1):
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


def get_points(k, keys):
    # points = 0
    # for i in ALL_KEYS:  # len(ALL_KEYS)
    #     if 0 < keys.count(i) <= k:  # len(keys)`
    #         points += 1
    # return points

    # score = 0
    # for value in keys.values():  # O(N)
    #     if value <= total_keys_pressed:
    #         score += 1
    # return score
    return sum(x <= k for x in keys.values())
    # return sum(0 < keys.count(x) <= k for x in ALL_KEYS)


if __name__ == "__main__":
    input_k = int(input())*2
    # keys_on_board = ''
    # for i in range(4):
    #     keys_on_board += input()

    input_keys = read_input()
    print(get_points(input_k, input_keys))
    # print(get_points(total_k, keys_on_board))
