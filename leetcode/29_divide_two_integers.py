class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = (dividend > 0) != (divisor > 0)

        dividend, divisor = abs(dividend), abs(divisor)
        count = 0

        tmp = divisor
        while (divisor <= dividend):
            _count = 1
            while (tmp << 1 <= dividend):
                tmp <<= 1
                _count <<= 1
            dividend -= tmp
            tmp = divisor
            count += _count

        if flag: # differend signs
            return max(-count, -2**31)
        else: # same signs
            return min(count, 2**31 - 1)

                

sol = Solution()
a, b = (int(x) for x in input().split())
print(sol.divide(a, b))