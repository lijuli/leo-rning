days_total = int(input())
temperature_values = [int(x) for x in input().split()]


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
