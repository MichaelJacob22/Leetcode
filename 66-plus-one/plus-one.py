class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string=""
        for i in digits:
            string+=str(i)
        
        string=int(string)
        string+=1
        digits=[]
        for i in str(string):
            digits.append(int(i))
        
        return digits

