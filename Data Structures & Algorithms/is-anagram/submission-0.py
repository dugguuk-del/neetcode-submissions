class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_1 = [s[i] for i in range(len(s))]
        s_2 = [t[i] for i in range(len(t))]
        s_1.sort()
        s_2.sort()
        a=s_1==s_2
        return a        