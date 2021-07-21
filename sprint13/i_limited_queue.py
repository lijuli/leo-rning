class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, item):
        if self.size != self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.size != 0:
            item = self.queue[self.head]
            self.head = (self.head + 1) % self.max_n
            self.size -= 1
            print(item)
        else:
            print(None)

    def peek(self):
        if self.size != 0:
            print(self.queue[self.head])
        else:
            print('None')

    def read_instruction(self, instruction):
        if 'push' in instruction:
            item = int(instruction[1])
            return self.push(item)
        if 'pop' in instruction:
            return self.pop()
        if 'peek' in instruction:
            return self.peek()
        if 'size' in instruction:
            print(self.size)


if __name__ == "__main__":
    number_of_instructions = int(input())
    max_queue_size = int(input())
    queue = MyQueueSized(max_queue_size)
    for i in range(number_of_instructions):
        instruction = [x for x in input().split()]
        queue.read_instruction(instruction)
