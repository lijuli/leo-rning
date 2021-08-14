# https://contest.yandex.ru/contest/24735/run-report/52292957/
import dis

class Competitor:
    """
    Class that holds information about competitor in competition or game.

    Attributes:
        name: A string for Competitor name.
        solutions: An integer count of problems solved.
        penalty: An integer count of penalties received.
        standing: A list of attributes used as cumulative score.
    """

    def __init__(self, name: str, solutions: int, penalty: int) -> None:
        """Initializes Competitor class."""
        self.name = name
        self.solutions = solutions
        self.penalty = penalty
        self.standing = (-self.solutions, self.penalty, self.name)

    def __gt__(self, other: 'Competitor') -> bool:
        """
        Implements comparison between two competitors
        using lexicographical ordering.
        """
        return self.standing > other.standing


def quick_sort(arr: list, left: int, right: int):
    """Implements in-place quick sort algorithm."""
    if left < right:
        def partition(arr: list, left: int, right: int) -> int:
            """Implements Lomuto partition algorithm."""
            pivot = arr[right]
            for index in range(left, right):
                if pivot.__gt__(arr[index]):
                    arr[index], arr[left] = arr[left], arr[index]
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
    dis.dis(Competitor.__gt__)