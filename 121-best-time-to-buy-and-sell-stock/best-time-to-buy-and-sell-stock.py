class Solution:
    def maxProfit(self, prices):
        min=prices[0]
        max =0
        profit=0
        a=0
        for i in prices:
            if(min>=i):
                min=i
            a=i-min
            if(profit<=a):
                profit=a
        return profit
        