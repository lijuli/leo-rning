class Stack:
    def __init__(self):
        self.items = []

    OPERATIONS = {
        '+': lambda a, b: b + a,
        '-': lambda a, b: b - a,
        '*': lambda a, b: b * a,
        '/': lambda a, b: b // a
    }

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError as error:
            print(f'pop from empty stack error:, {error}')

    def calculate(self, expression):
        for char in expression.split():
            self.push(self.calculate_char(char))
        return self.pop()

    def calculate_char(self, char):
        if char in self.OPERATIONS:
            a = self.pop()
            b = self.pop()
            operator = self.OPERATIONS[char]
            return operator(a, b)
        else:
            return int(char)


if __name__ == '__main__':
    s = Stack()
    result = s.calculate(input())
    print(result)
