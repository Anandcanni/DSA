class Solution:
    #anand
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        longest = 1
        counter = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i -1] + 1:
                counter += 1
            elif nums[i] != nums[i -1]:
                counter = 1
           
            
            longest =max(longest,counter)
        return longest

