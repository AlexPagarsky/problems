class Solution:

    def shift(self, s, shift):
        if not shift: return s
        shift %= len(s)
        return s[-shift:] + s[:-shift]

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final = 0

        for step in shift:
            final += step[1] if step[0] else -step[1]

        return self.shift(s, final)