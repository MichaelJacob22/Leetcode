class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[0]*(amount+1) for _ in range(len(coins))]

        for row in range(amount+1):
            if row % coins[0] == 0:
                dp[0][row]=1
            
        for col in range(len(coins)):
            dp[col][0]=1
        
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if not(j-coins[i]<0):
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]