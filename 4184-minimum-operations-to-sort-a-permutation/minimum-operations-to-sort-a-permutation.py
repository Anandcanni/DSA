class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        start = nums.index(0)
        inc = True
        dec= True
        for i in range(1,n):
            value = nums[(start + i)% n]
            if value != i:
                inc =False
            if value != n-i:
                dec = False
            if not inc and not dec:
                return  -1
        if inc:
            return min(start,n-start+2)
        return min(n-start,start+2)