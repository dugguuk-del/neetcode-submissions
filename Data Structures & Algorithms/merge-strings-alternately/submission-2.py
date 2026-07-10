class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)>=len(word2):
            e = len(word2)
            big = word1
            small = word2
            for i in range(e):
                big = big[:2*i+1] + small[i] + big[2*i+1:]
            return big 

        if len(word1)<len(word2):
            e = len(word1)
            big = word2
            small = word1
            f = ""
            for i in range(e):
                f+= small[i] + big[i]
            f+= big[e:]
            return f