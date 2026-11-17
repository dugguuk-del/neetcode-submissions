class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        a = Counter(s)
        b = Counter(t)
        return a==b      