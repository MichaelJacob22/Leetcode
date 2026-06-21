class Solution:
    def reverseWords(self, s):
        b = s.split()
        a = ""

        for i in range(len(b)-1, -1, -1):
            a += b[i]
            if i != 0:
                a += " "

        return a