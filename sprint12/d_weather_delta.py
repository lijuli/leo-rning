#  4

days_total = int(input())
temperature_values = [int(x) for x in input().split()]


# def compare_corner_values(value, other_value):
#     return value > other_value
#
#
# def get_delta_counts(array, length):
#     count = 1
#     for i in range(1, length - 1):
#         current = array[i]
#         if current > array[i - 1] and current > array[i + 1]:
#             count += 1
#     return count
#
#
# def get_weather_delta(array, length):
#     if length == 0:
#         return 0
#     count = get_delta_counts(array, length)
#     count += compare_corner_values(array[0], array[1])
#     count += compare_corner_values(array[-1], array[-2])
#     return count


def get_value(array, length, i, current):
    if 0 < i < length:
        return array[i] < current
    return True


def get_weather_delta(array, length):
    count = 0
    for i in range(length):
        current = array[i]
        if get_value(array, length, i-1, current) and get_value(array, length, i+1, current):
            count += 1
    return count


print(get_weather_delta(temperature_values, days_total))
