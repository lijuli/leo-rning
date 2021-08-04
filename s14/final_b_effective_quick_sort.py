# https://contest.yandex.ru/contest/24735/run-report/52285873/

class Competitor:
    def __init__(self, name, solutions, penalty):
        self.name = name
        self.solutions = solutions
        self.penalty = penalty
        self.standing = (-self.solutions, self.penalty, self.name)

    def compare(self, other):
        return self.standing > other.standing


def quick_sort(arr, left, right):
    if left < right:
        def partition(arr, left, right):
            pivot = arr[right]
            for i in range(left, right):
                if pivot.compare(arr[i]):
                    arr[i], arr[left] = arr[left], arr[i]
                    left += 1

            arr[left], arr[right] = arr[right], arr[left]
            return left

        border = partition(arr, left, right)

        quick_sort(arr, left, border - 1)
        quick_sort(arr, border + 1, right)


if __name__ == "__main__":
    competitors = []
    competitors_count = int(input())
    for _ in range(competitors_count):
        competitor_input = input().split()

        competitor = Competitor(
            competitor_input[0],
            int(competitor_input[1]),
            int(competitor_input[2])
        )

        competitors.append(competitor)

    quick_sort(competitors, 0, competitors_count - 1)
    for competitor in competitors:
        print(competitor.name)
