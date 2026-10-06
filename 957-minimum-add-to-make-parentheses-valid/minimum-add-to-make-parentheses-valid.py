class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        _1open = 0
        ans = 0

        for ch in s:
            if ch == '(':
                _1open += 1
            else:
                if _1open:
                    _1open -= 1
                else:
                    ans += 1

        return ans + _1open