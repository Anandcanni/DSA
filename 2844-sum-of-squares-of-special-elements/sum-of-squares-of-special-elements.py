class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        sum_1 = []
        for i in range(1,n+1):
            if n % i == 0:
                sum_1.append(nums[i-1]*nums[i-1])
        return sum(sum_1)
