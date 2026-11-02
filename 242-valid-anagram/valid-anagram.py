from collections import Counter
class Solution:
    #Anand
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        
      