class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: return num
        if num==10: return 1
        digit = []
        while num > 10:
            temp = int(num%10)
            num = int(num/10)
            digit.append(temp)
        digit.append(num)
        return self.addDigits(sum(digit))


sol = Solution()


print(sol.addDigits(int(input())))