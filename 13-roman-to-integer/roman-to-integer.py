class Solution:
    def romanToInt(self, s):
        b=0
        for i in range(0,len(s),1):
            if(s[i]=='I'):
                b+=1
            elif(s[i]=='V'):
                if((i!=0)and(s[i-1]=='I')):
                    b+=3
                else:
                    b+=5
            elif(s[i]=='X'):
                if((i!=0)and(s[i-1]=='I')):
                    b+=8
                else:
                    b+=10
            elif(s[i]=='L'):
                if((i!=0)and(s[i-1]=='X')):
                    b+=30
                else:
                    b+=50
            elif(s[i]=='C'):
                if((i!=0)and(s[i-1]=='X')):
                    b+=80
                else:
                    b+=100
            elif(s[i]=='D'):
                if((i!=0)and(s[i-1]=='C')):
                    b+=300
                else:
                    b+=500
            else:
                if((i!=0)and(s[i-1]=='C')):
                    b+=800
                else:
                    b+=1000
        return b

        