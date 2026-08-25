class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for i in asteroids:
            while stk and i<0 and stk[-1] > 0:
                diff = i + stk[-1]
                if diff>0:
                    i = 0
                elif diff<0:
                    stk.pop()
                else:
                    stk.pop()
                    i=0
            if i:
                stk.append(i)
        return stk
