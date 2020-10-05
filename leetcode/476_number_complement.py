class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int('1' * len(bin(n)[2:]), 2) ^ n
