class Solution:
    # fibonacci
    
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1                 
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one 
    
    # recursion with memoization
    
#     def climb_stairs(self, i, n, memo):
#         if i > n:
#             return 0
#         if i == n:
#             return 1
#         if memo[i] > 0:
#             return memo[i]
#         memo[i] = self.climb_stairs(i+1, n, memo) + self.climb_stairs(i+2, n, memo)
        
#         return memo[i]
    
#     def climbStairs(self, n: int) -> int:
#         memo = [0]*n
#         return self.climb_stairs(0, n, memo)
    
    # dp method with memoization
    
#     def climbStairs(self, n: int) -> int:
#         dp = [0]*(n+1)
        
#         if n == 1:
#             return 1
        
#         dp[1] = 1
#         dp[2] = 2
        
#         for i in range(3, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
        
#         return dp[n]
        