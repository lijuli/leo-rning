class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]


def combine_segments(arr, st):
    arr.sort()
    st.push(arr[0])

    for i in range(1, len(arr)):
        temp = st.peek()
        if temp[1] >= arr[i][0]:
            st.pop()
            st.push([temp[0], max(arr[i][1], temp[1])])
        else:
            st.push(arr[i])

    return st.items


if __name__ == "__main__":
    st = StackMax()
    result = combine_segments(
        [list(map(int, input().split())) for _ in range(int(input()))],
        st
    )
    [print(*item) for item in result]
