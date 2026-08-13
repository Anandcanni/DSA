class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c =0
        jewels = set([i for i in jewels])
        for s in stones:
            if s  in jewels:
                c += 1
        return c
        