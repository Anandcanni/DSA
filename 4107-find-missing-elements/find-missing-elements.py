class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mx =max(nums)
        mn  = min(nums)
        seen =set(nums)
        ans =[]

        for i in range(mn+1,mx):
            if i not in seen:
                ans.append(i)
        return ans


        