def find_distances_to_empty_spots(spots):
    distances = [None] * len(spots)
    empty_spot = -1
    for index in range(len(spots)):
        if spots[index] == '0':
            empty_spot = index
            distances[index] = 0
            continue
        if empty_spot == -1:
            continue
        distances[index] = abs(index - empty_spot)

    for index in range(empty_spot - 1, -1, -1):
        if spots[index] == '0':
            empty_spot = index
            continue
        distance = abs(index - empty_spot)
        if distances[index] is None or distance < distances[index]:
            distances[index] = distance
    return distances


if __name__ == "__main__":
    input()
    houses = [x for x in input().split()]
    distances = find_distances_to_empty_spots(houses)
    print(*distances)
