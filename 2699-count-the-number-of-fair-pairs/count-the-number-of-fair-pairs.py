class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1
            while l<=r:
                mid = (l+r)//2
                if nums[i]+nums[mid] >= lower:
                    r = mid - 1
                else:
                    l = mid + 1
            left = l
            l = i+1 
            r = len(nums) - 1
            while l<=r:
                mid = (l+r)//2
                if nums[i]+nums[mid] > upper:
                    r = mid - 1
                else:
                    l = mid + 1
            right = l
            count += right - left
        return count
            






        