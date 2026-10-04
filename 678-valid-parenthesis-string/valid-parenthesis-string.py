class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        star = []
        for i in range(len(s)):
            if s[i] =='(':
                stk.append(i)
            elif s[i]=='*':
                star.append(i)
            else:
                if stk:
                    stk.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while stk and star:
            if stk[-1] > star[-1]:
                return False
            
            star.pop()
            stk.pop()
        return not stk
        