class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i
        for i in range(len(nums)):
            c =target -nums[i]
            if c in seen and seen[c] != i:
                return [i,seen[c]]
        return []