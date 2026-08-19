class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtrack(s,op,cl):
            if len(s)==n*2:
                ans.append(s)
                return
            
            if op<n:
                backtrack(s+"(",op+1,cl)
            if cl<op:
                backtrack(s+")",op,cl+1)
            
        backtrack("",0,0)
        return ans