class Solution:
    def climbStairs(self, n: int) -> int:
        f = 1
        s = 2
        t = 0

        for i in range(n + 1):
            if i < 3:
                continue

            t = f + s
            f = s
            s = t

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return t
