class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        if len(nums) == 0:
            return False
        if len(s) < len(nums):
            return True
        else:
            return False
        