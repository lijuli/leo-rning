class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    def put(self, element):
        temp = Node(element)
        if self.count == 0:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.count += 1

    def get(self):
        if self.count != 0:
            print(self.head.value)
            self.head = self.head.next
            self.count -= 1
        else:
            print('error')

    def size(self):
        print(self.count)

    def read_instruction(self, call):
        if 'get' in call:
            return self.get()
        if 'put' in call:
            item = int(call[1])
            return self.put(item)
        if 'size' in call:
            return self.size()


if __name__ == "__main__":
    number_of_instructions = int(input())
    queue = Queue()
    for i in range(number_of_instructions):
        instruction = [x for x in input().split()]
        queue.read_instruction(instruction)
