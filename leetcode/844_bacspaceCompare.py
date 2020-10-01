from collections import deque

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        first = deque()
        second = deque()

        for i in S:
            if i != '#':     first.append(i)
            elif len(first): first.pop()

        for j in T:
            if j != '#':      second.append(j)
            elif len(second): second.pop()
        
        for i in reversed(first):
            if i != second.pop(): return False
        
        return True

