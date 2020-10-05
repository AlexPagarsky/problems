from collections import deque

class MinStack:

    class Node:
        def __init__(self, value, m):
            self.value = value
            self.m = m

    def __init__(self):
        self.arr = deque()

    def push(self, x: int) -> None:
        if len(self.arr):
            m = self.getMin()
            self.arr.append(self.Node(x, min(x, m)))
        else:
            self.arr.append(self.Node(x, x))

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        res = self.arr.pop()
        self.arr.append(res)

        return res.value

    def getMin(self) -> int:
        temp = self.arr.pop()
        self.arr.append(temp)

        return temp.m

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    m = MinStack()
    m.push(-2)
    m.push(0)
    m.push(-3)
    print(m.getMin())
    m.pop()
    print(m.top())
    print(m.getMin())