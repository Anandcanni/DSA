class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res , sol =[],[]
        def backtrack (i , j):
            if len(sol) == 2*n:
                res.append(''.join(sol))
                return
            if  i < n:
                sol.append('(')
                backtrack(i+1,j)
                sol.pop()
            if  i>j:
                sol.append(')')
                backtrack(i,j+1)
                sol.pop()
        backtrack(0,0)
        return res
        