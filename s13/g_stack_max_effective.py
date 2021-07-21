class StackMax:
    def __init__(self):
        self.items = []
        self.sorted_items = []

    def push(self, item):
        self.items.append(item)
        if not self.sorted_items:
            self.sorted_items.append(item)
        else:
            self.sorted_items.append(max(item, self.sorted_items[-1]))

    def pop(self):
        if self.items:
            self.sorted_items.pop()
            return self.items.pop()
        else:
            print('error')

    def peek(self):
        if self.items:
            return self.items[-1]

    def get_max(self):
        if self.items:
            print(self.sorted_items[-1])
        else:
            print(None)

    def read_instruction(self, instruction):
        if 'push' in instruction:
            item = int(instruction[1])
            return self.push(item)
        if 'pop' in instruction:
            return self.pop()
        if 'get_max' in instruction:
            return self.get_max()


if __name__ == "__main__":
    stack = StackMax()
    number_of_instructions = int(input())
    for i in range(number_of_instructions):
        instruction = [x for x in input().split()]
        stack.read_instruction(instruction)
