
        
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            needed = sum(max(d - mid, 0) for d in diff)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        # Reduce every difference to at most left
        for i, d in enumerate(diff):
            reduction = max(0, d - left)
            k -= reduction
            diff[i] = min(d, left)

        # Use remaining operations to reduce values equal to left
        for i in range(len(diff)):
            if k == 0:
                break
            if diff[i] == left:
                diff[i] -= 1
                k -= 1

        return sum(d * d for d in diff)

        