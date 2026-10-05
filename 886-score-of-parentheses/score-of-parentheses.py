class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]
        
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(0)
            else:
                x = stk.pop()
                
                if x == 0:
                    score = 1
                else:
                    score =2 *x 
                stk[-1] += score
        return stk[0]

        