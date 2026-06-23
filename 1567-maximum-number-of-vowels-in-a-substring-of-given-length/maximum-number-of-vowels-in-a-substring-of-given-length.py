class Solution:
    def maxVowels(self, s, k):
        v="aeiou"
        c=0
        for i in range(k):
            if s[i] in v:
                c+=1
        m=c
        p=0
        l=k
        while l<len(s):

            if s[p] in v:
                c-=1
            
            if s[l] in v:
                c+=1
            m=max(c,m)
            p+=1
            l+=1

        return m