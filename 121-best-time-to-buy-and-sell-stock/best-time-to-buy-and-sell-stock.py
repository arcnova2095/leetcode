class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest= prices[0]
        maxp=0
        for i in prices:
            lowest= min(lowest,i)
            maxp=max(maxp,i-lowest)
        return maxp