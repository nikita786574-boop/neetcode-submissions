class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_minimum = []
    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.stack_minimum) > 0:
            if self.stack_minimum[-1] >= value:
                self.stack_minimum.append(value)
        else:
            self.stack_minimum.append(value)
    def pop(self) -> None:
        value = self.stack[-1]
        del self.stack[-1]
        if self.stack_minimum[-1] == value:
            del self.stack_minimum[-1]
        return value
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack_minimum) == 0:
            return None
        return self.stack_minimum[-1]
        
