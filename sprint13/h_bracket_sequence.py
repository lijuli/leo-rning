class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_correct_bracket_seq(self, sequence):
        for bracket in sequence:
            if bracket in '{([':
                self.push(bracket)
                continue
            if (self.size() and (
                    self.peek() == '{' and bracket == '}' or
                    self.peek() == '(' and bracket == ')' or
                    self.peek() == '[' and bracket == ']'
            )):
                self.pop()
            else:
                return False
        return not self.size()


if __name__ == "__main__":
    stack = Stack()
    brackets = input()
    print(stack.is_correct_bracket_seq(brackets))
