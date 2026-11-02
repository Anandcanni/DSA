class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen ,dup = set() ,set()
        for i in nums:
            if i in seen:
                dup.add(i)
            seen.add(i)
        return list(dup)