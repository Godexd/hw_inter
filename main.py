BRACKETS = {'(': ')', '{': '}', '[': ']'}


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        length = self.size()
        return length == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        length = self.size()
        if length:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def is_balanced(self, string):
        string_length = len(string)
        for number, element in enumerate(string, start=1):

            if element in BRACKETS.keys():
                self.push(element)
            elif element in BRACKETS.values():
                if BRACKETS.get(self.peek()) == element:
                    self.pop()
                else:
                    return f'string {string} не сбалансированно'
            if self.is_empty() and number == string_length:
                return f'string {string} сбалансированно'
            elif not self.is_empty() and number == string_length:
                return f'string {string} не сбалансированно'


if __name__ == '__main__':
    strings = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
    item = Stack()
    for s in strings:
        print(item.is_balanced(s))