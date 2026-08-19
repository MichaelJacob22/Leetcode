class Solution:
    def letterCombinations(self, digits):
        ans=[]
        ph_no={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        def backtrack(s,i):
            if i==len(digits):
                ans.append(s)
                return
            
            p=ph_no[digits[i]]

            for j in p:
                backtrack(s+j,i+1)
            
        backtrack("",0)
        return ans