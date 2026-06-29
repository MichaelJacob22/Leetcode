class Solution:
    def lengthOfLongestSubstring(self, s):
        b=[]
        m=0
        for k in range(0,len(s),1):
            if(s[k] not in b):
                m=max(len(b)+1,m)
            else:
                while s[k] in b:
                    b.remove(b[0])
            b.append(s[k])
        return m
        