"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
            graph={}
            for emp in employees:
                graph[emp.id]=emp

            def dfs(node):
                emp=graph[node]

                total=emp.importance

                for nei in emp.subordinates:
                    total+=dfs(nei)
                
                return total
            
            ans=dfs(id)
            return ans