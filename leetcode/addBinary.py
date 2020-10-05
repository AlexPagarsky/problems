class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = int(a, 2)
        j = int(b, 2)
        val = i + j
        val = str(bin(val))
        return val[2::]

sol = Solution()


print(sol.addBinary(11, 1))
