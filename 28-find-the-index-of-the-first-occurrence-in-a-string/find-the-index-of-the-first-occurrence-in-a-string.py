class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        j=len(needle)
        c=""
        for k in range(len(haystack)-len(needle)+1):
            c="".join(haystack[i:j])
            print (c)
            if c==needle:
                return i
            i+=1
            j+=1
        return -1