from math import comb
class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        if n % 2 == 0:
            j = int(n / 2)
            for i in range(0, n + 1, 2):
                ans += comb(j, i)
                j += 1
        else:
            j = int((n/2)+1)
            ans += 1
            for i in range(1, n - 1, 2):
                ans += comb(j,i)
                j += 1
        return ans