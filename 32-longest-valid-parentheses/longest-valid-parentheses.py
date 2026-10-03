class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #hashmap = {')':'('}
        stk = [-1]
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    count = max(count, i - stk[-1])
        return count
