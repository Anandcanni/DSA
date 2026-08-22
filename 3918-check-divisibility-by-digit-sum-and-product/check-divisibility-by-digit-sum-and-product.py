class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)
        a = len(s)
        x = 0
        y = 1
        for i in range(a):
            x = x + int(s[i])
            y = y * int(s[i])
        if n % (x+y) == 0:
            return True
        else:
            return False

        