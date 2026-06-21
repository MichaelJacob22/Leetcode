class Solution:
    def maximumWealth(self, accounts):
        c=[sum(i) for i in accounts]
        a=0
        for i in range(0,len(accounts),1):
            if(a<=int(c[i])):
                a=int(c[i])
        return a