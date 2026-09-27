import math
class Stack(list):
    def pop(self):
        if len(self) == 0:
            return None
        value = self[-1]
        del self[-1]
        return value
    def top(self):
        if len(self) == 0:
            return None
        return self[-1]
    def push(self, value):
        self.append(value)

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = Stack()
        count_digits = 0
        index = len(tokens) - 1
        operations = {'+': lambda x, y: x + y,
                        '-': lambda x, y: x - y,
                        '*': lambda x, y: x * y,
                        '/': lambda x, y: x / y}
        while True:
            if count_digits == 2:
                digit1 = stack.pop()
                digit2 = stack.pop()
                math_symbol = stack.pop()
                top = stack.top()
                stack.push(str(int(operations[math_symbol](float(digit1), float(digit2)))))
                if top == None:
                    count_digits = 1
                elif top in '+-*/':
                    count_digits = 1
                else:
                    count_digits = 2
                if index < 0 and len(stack) == 1:
                    break
            else:
                value = tokens[index]
                if value in '+-*/':
                    count_digits = 0
                else:
                    count_digits += 1
                stack.push(value)
                index -= 1
                if index == -1 and len(stack) == 1:
                    break
        
        return int(float(stack.pop()))
            