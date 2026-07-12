class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        poty = []
        for i in range(len(prices)):
            a = prices[i]
            for j in prices[i+1:]:
                poty.append(j-a)
        c = max(poty)
        if c>0:
            return c
        else:
            return 0 
