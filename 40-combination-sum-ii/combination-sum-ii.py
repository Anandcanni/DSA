class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        res , sol = [],[]
        n = len(nums)
        def backtrack(i , total):
            if  total == target:
                res.append(sol[:])
                return
            if total > target or i == n:
                return
            #include
            sol.append(nums[i])
            backtrack(i+1,total + nums[i])
            sol.pop()
            #skip
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1,total)
        backtrack(0,0)
        return res