class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        l = 0
        window_count = {}      # only reflects current window
        universal_count = {}       # cumulative across whole array (if you need it separately)
        

        for r in range(len(nums)):
        # add incoming element to both dicts
            window_count[nums[r]] = window_count.get(nums[r], 0) + 1
        

            if r - l + 1 == k:
            # window is full-size: check it
                for x in window_count:
                    universal_count[x] = universal_count.get(x, 0) + 1
                        

            # remove the element that's about to fall out of the window
                window_count[nums[l]] -= 1
                if window_count[nums[l]] == 0:
                    del window_count[nums[l]]
                l += 1
        ans = -1
        for x in universal_count:
            if universal_count[x] == 1:
                ans = max(ans, x)

        return ans
            
        