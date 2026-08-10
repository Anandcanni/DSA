class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n =len(nums)
        res =[]
        def backtrack(start):
            if start == n:
                res.append(nums[:])
                return
            unq = set()
            for i in range(start,n):
                if nums[i] in unq:
                    continue
                unq.add(nums[i])
                nums[start] , nums[i]= nums[i],nums[start]
                backtrack(start+1)
                nums[start] , nums[i]= nums[i],nums[start]
        backtrack(0)
        return res


        