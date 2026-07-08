class Solution:
    def longestPalindromeSubseq(self, s):
        t=s[::-1]
        dp=[[0]*(len(s)+1) for _ in range(len(s)+1)]

        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[-1][-1]