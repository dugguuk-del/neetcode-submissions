class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l=0
        r=1
        a = set(s[l])
        c=1
        while r<=len(s)-1:
            if s[r] in a:
                while s[r] in a:
                    a.remove(s[l])
                    l+=1
                a.add(s[r])
            else:
                a.add(s[r])
            c=max(c,r-l+1)
            r+=1
        return c
