class Solution:
    def isPalindrome(self, s):
        c=""
        for i in range(0,len(s),1):
            if(s[i].isalpha()):
                c+=s[i].lower()
            elif(s[i].isdigit()):
                c+=s[i]
        if(c==c[::-1]):
            return True
        else:
            return False
        