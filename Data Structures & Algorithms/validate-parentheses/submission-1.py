class Stack(list):
    def pop(self):
        item = None
        if len(self) > 0:
            item = self[-1]
            del self[-1]
        return item
    def push(self, item):
        self.append(item)
    def top(self):
        return self[-1]
class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        mapa = {']':'[', '}':'{', ')':'('}
        for item in s:
            if item in ')]}':
                last_item = stack.pop()
                if not last_item or last_item != mapa[item]:
                    return False
                
            else:
                stack.push(item)
        if len(stack) == 0:
            return True
        return False