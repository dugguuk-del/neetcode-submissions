class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = False
        dict1 = {i:s1.count(i) for i in s1}
        for i in range(len(s2)-len(s1)+1):
            dict2 = {j:s2[i:i+len(s1)].count(j) for j in s2[i:i+len(s1)]}
            if dict1==dict2:
                c = True
                break
        return c