class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        l=0
        best=0
        for r in range(len(s)):
            if s[r] in sub:
                sub = sub[sub.rfind(s[r])+1:]
            if s[r] not in sub:
                sub+=s[r]
            if len(sub)>best:
                best=len(sub)
        return best