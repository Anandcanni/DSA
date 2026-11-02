class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n =len(nums)
        if n==1:
            return  0
        nums.sort()
        mid =nums[n//2]
        res =0
        for i in nums:
            res+=abs(i-mid)
        return res
        