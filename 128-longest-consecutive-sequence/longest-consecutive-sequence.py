class Solution:
    #anand
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for nums in s:
            if nums-1 not in s:
                curr =1
                while nums+1 in s:
                    curr += 1
                    nums += 1
                longest = max(longest,curr)
        return longest
       

        