class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelset = {'a','e','i','o','u'}
        l = 0
        n = len(s)
        curr =0
        ans  = 0
        for r in range (len(s)):
            curr += 1 if s[r] in vowelset else 0
            if r - l +1 > k:
                curr -= 1 if s[l] in vowelset else 0
                l+= 1
            ans = max(curr, ans)
        return ans

