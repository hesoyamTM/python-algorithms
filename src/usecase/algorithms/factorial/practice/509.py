class Solution:
    def fib(self, n: int) -> int:
        f = 0
        s = 1
        t = 0

        for _ in range(n - 1):
            t = f + s
            f = s
            s = t

        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return t
