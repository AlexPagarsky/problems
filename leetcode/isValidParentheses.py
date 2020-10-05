class Solution:
    def isValid(self, s: str) -> bool:

        values = {
            '}' : '{',
            ')' : '(',
            ']' : '[',
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }
        stack = list()
        for i in s:
            if values[i] not in stack or len(stack) == 0:
                stack.append(i)
            elif values[i] in stack:
                stack.pop()

        return len(stack) == 0



sol = Solution()

print(sol.isValid(input()))




# ({[]})