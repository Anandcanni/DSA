class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        def backtrack(i , curr):
            if i == n:
                res.append(curr[:])
                return
            #if subset has nums[i]
            curr.append(nums[i])
            backtrack(i+1 , curr)
            curr.pop()
            #uf subset has not nums[i]
            while i+1<n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1,curr)
        backtrack(0,[])
        return res

        