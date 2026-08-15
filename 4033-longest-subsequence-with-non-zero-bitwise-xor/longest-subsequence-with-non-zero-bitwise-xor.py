class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x = 0

        if all(i == 0 for i in nums):
            return 0

        for l in nums:
            x ^= l

        if x != 0:
            return len(nums)

        return len(nums) - 1
        