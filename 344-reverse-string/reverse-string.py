class Solution:
    def reverseString(self, s):
        i=0
        j=len(s)-1
        for k in range(0,int(len(s)/2),1):
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        
        