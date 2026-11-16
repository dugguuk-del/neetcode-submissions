class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        l=0
        r=l+1
        a = prices[r]-prices[l]
        c=a
        while r<=len(prices)-1:
            if prices[r]>prices[l]:
                a = prices[r]-prices[l]
                c = max(c,a)
                r+=1
            else:
                l=r
                r=l+1
        if c<0:
            return 0
        return c   
            
