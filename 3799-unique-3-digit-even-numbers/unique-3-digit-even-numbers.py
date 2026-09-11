class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans=set()
        for i in range(len(digits)):
            if digits[i]!=0:
                for j in range(len(digits)):
                    if i!=j:
                        for k in range(len(digits)):
                            if digits[k]%2==0 and i!=k and j!=k:
                                ans.add(digits[i]*100+digits[j]*10+digits[k])
        print(ans,sep=" ")
        return len(ans)