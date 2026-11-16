class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a = {}
        l=0
        r=0
        n=0        
        b=0
        while r<=len(s)-1:
            if s[r] not in a:
                n+=1
                a[s[r]]=0
            a[s[r]]+=1
            r+=1
            if sum(list(a.values()))-max(list(a.values()))<=k:
                b=max(b,r-l)
            if sum(list(a.values()))-max(list(a.values()))>k:
                a[s[l]]-=1
                l+=1
            if len(a)==1:
                b=max(b,r-l)
        return b
            