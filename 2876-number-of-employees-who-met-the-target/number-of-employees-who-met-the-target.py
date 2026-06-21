class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        c=0
        for i in hours:
            if(i>=target):
                    c+=1
        return c
  