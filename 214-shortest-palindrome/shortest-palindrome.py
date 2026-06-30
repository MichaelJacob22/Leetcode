class Solution:
    def shortestPalindrome(self, s: str) -> str:
        j=len(s)
        if s=="":
            return ""
        for i in range(len(s)):
            c=s[j:len(s)]
            c=c[::-1]+s
            if(c==c[::-1]):
                return c
            j-=1