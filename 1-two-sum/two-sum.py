class Solution:   
    def twoSum(self,c,g):
        for i in range(0,len(c),1):
            for j in range(i+1,len(c),1):
                if((c[i]+c[j])==g):
                    return [i,j]