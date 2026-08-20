class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a = asteroids
        l = 1

        while l < len(a):

            if a[l] > 0:
                l += 1

            else:
                if l > 0 and a[l-1] > 0:

                    if abs(a[l]) > abs(a[l-1]):
                        a.pop(l-1)
                        l -= 1

                    elif abs(a[l]) < abs(a[l-1]):
                        a.pop(l)
                        if l >= len(a):
                            break

                    else:
                        a.pop(l)
                        a.pop(l-1)
                        l -= 1

                else:
                    l += 1

        return a