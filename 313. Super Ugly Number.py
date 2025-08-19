class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        primelen = len(primes)
        dp = [1] * n

        factor_index = [0] * primelen 
        factor_value = primes[:]

        for i in range(1, n):
            dp[i] = min(factor_value)

            for j in range(primelen):
                if factor_value[j] == dp[i]:
                    factor_index[j] += 1
                    factor_value[j] = primes[j] * dp[factor_index[j]]
        return dp[n-1]