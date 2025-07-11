# // Time Complexity : O(n * m)
# // Space Complexity : O(n)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # converted 2D dp array to 1D
        # use 2D array to arrive at solution and convert it to 1D array for optimization.
        dp = [0 for i in range(amount+1)]
        dp[0] = 1 

        for i in coins:
            for j in range(i,amount+1):
                dp[j] = dp[j-i] + dp[j]
        return(dp[-1])
                
   
