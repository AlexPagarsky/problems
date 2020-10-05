class MyQueue:

    def __init__(self):
        self.body = list()
        

    def push(self, x: int) -> None:
        self.body.append(x)
        

    def pop(self) -> int:
        return self.body.pop()
        

    def peek(self) -> int:
        if len(self.body) != 0:
            return self.body.pop(0)
        else:
            return None
        

    def empty(self) -> bool:
        return len(self.body) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



obj = MyQueue()
print(obj.push(1), 1)
print(obj.pop(), 2)
print(obj.peek(), 3)
print(obj.empty(), 4)