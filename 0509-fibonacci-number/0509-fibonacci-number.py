class Solution:
    def fib(
        self,
        n: int,
    ) -> int:
        dp = [0] * (n + 1)
        return self.rec(n, dp)

    def rec(self, n, dp):
        if n == 0 or n == 1:
            return n
        if dp[n] != 0:
            return dp[n]
        dp[n] = self.rec(n - 1, dp) + self.rec(n - 2, dp)
        return dp[n]
