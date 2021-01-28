class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        out = [ord('a')] * n
        
        if k == n:
            return ''.join(chr(i) for i in out)

        cost = n
        i = n - 1

        while cost < k and i >= 0:
            # print(''.join(chr(j) for j in out), cost, i)
            cost += ord('z') - out[i]
            out[i] = ord('z')
            i -= 1

        if i < 0:
            i = 0

        while cost > k:
            # print(''.join(chr(j) for j in out), cost, i)
            if out[i] == ord('a'):
                i += 1
            out[i] -= 1
            cost -= 1

        return ''.join(chr(j) for j in out)
