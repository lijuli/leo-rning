class Deque:
    def __init__(self, n):
        self.deque = [None] * n
        self.head = 0
        self.tail = 0
        self.max_n = n
        self.size = 0

    def push_front(self, value):
        if self.size == self.max_n:
            raise IndexError

        if self.size == 0:
            self.deque[self.head] = value
            self.size += 1
        else:
            self.head = (self.head - 1) % self.max_n
            self.deque[self.head] = value
            self.size += 1

    def push_back(self, value):
        if self.size == self.max_n:
            raise IndexError

        if self.size == 0:
            self.deque[self.tail] = value
            self.size += 1
        else:
            self.tail = (self.tail + 1) % self.max_n
            self.deque[self.tail] = value
            self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError

        value = self.deque[self.tail]
        self.deque[self.tail] = None
        self.size -= 1

        if self.size == 0:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail - 1) % self.max_n
        return value

    def pop_front(self):
        if self.size == 0:
            raise IndexError

        value = self.deque[self.head]
        self.deque[self.head] = None
        self.size -= 1
        if self.size == 0:
            self.head = 0
            self.tail = 0
        else:
            self.head = (self.head + 1) % self.max_n
        return value

    def read_instruction(self, call):
        if len(call) == 1:
            return getattr(self, call[0])()
        return getattr(self, call[0])(int(call[1]))


if __name__ == "__main__":
    number_of_instructions = int(input())
    max_dequeue_size = int(input())
    deque = Deque(max_dequeue_size)

    for _ in range(number_of_instructions):
        instruction = [x for x in input().split()]
        try:
            result = deque.read_instruction(instruction)
            if len(instruction) == 1:
                print(result)
        except IndexError:
            print('error')
            continue
