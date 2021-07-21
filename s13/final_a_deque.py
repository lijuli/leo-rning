# https://contest.yandex.ru/contest/23759/run-report/52197418/

class Deque:
    def __init__(self, n):
        self.deque = [None] * n
        self.head = 0
        self.tail = 0
        self.max_n = n
        self.size = 0

    def push_front(self, value):
        if self.size != self.max_n:
            if self.size == 0:
                self.deque[self.head] = value
                self.size += 1
            else:
                self.head = (self.head - 1) % self.max_n
                self.deque[self.head] = value
                self.size += 1
        else:
            print('error')

    def push_back(self, value):
        if self.size != self.max_n:
            if self.size == 0:
                self.deque[self.tail] = value
                self.size += 1
            else:
                self.tail = (self.tail + 1) % self.max_n
                self.deque[self.tail] = value
                self.size += 1
        else:
            print('error')

    def pop_back(self):
        if self.size != 0:
            value = self.deque[self.tail]
            print(value)

            self.deque[self.tail] = None
            self.size -= 1
            if self.size == 0:
                self.head = 0
                self.tail = 0
            else:
                self.tail = (self.tail - 1) % self.max_n
        else:
            print('error')

    def pop_front(self):
        if self.size != 0:
            value = self.deque[self.head]
            print(value)

            self.deque[self.head] = None
            self.size -= 1
            if self.size == 0:
                self.head = 0
                self.tail = 0
            else:
                self.head = (self.head + 1) % self.max_n
        else:
            print('error')

    def read_instruction(self, call):
        if 'push_back' in call:
            item = int(call[1])
            return self.push_back(item)
        if 'push_front' in call:
            item = int(call[1])
            return self.push_front(item)
        if 'pop_front' in call:
            return self.pop_front()
        if 'pop_back' in call:
            return self.pop_back()


if __name__ == "__main__":
    number_of_instructions = int(input())
    max_dequeue_size = int(input())
    deque = Deque(max_dequeue_size)

    for i in range(number_of_instructions):
        instruction = [x for x in input().split()]
        deque.read_instruction(instruction)
