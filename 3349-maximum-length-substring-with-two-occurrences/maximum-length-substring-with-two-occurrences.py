class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        a ={}
        l = 0
        curr =0
        ans =0
        for r in range(len(s)):
            if s[r] in a:
                a[s[r]] += 1
            else:
                a[s[r]] = 1
            curr = r - l + 1
            while a[s[r]] > 2:
                a[s[l]] -= 1
                l += 1
            curr = r - l + 1
            ans = max(ans, curr)
        return ans
        

        