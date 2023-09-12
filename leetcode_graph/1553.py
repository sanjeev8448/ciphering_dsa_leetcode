class Solution:
    def minDays(self, n: int) -> int:
        dp = {0:0,1:1}  # base case

        def dfs(n):
            if n in dp:
                return dp[n]
            
            one = 1 + (n % 2) + dfs(n // 2)
            print(one)
            two = 1 + (n % 3) + dfs(n // 3)
            print(two)
            dp[n] = min(one,two)
            return dp[n]
        return dfs(n)
    
s = Solution()
x = s.minDays(10)
print(x)