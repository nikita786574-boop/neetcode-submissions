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
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = Stack()
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            value = stack.pop()
            if value is None or temperatures[value] >= temperatures[i]:
                if value is not None:
                    stack.push(value)
                stack.push(i)
            else:
                while value is not None and temperatures[value] < temperatures[i]:
                    result[value] = i - value
                    value = stack.pop()
                if value is not None:
                    stack.push(value)
                stack.push(i)
        return result