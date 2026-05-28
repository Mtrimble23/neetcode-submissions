class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        mx = 0
        pf = 0
        for i in range(len(prices)):
            if prices[b] > prices[i]:
                b = i
            pf = prices[i] - prices[b]
            if pf > mx:
                mx = pf
        return mx
