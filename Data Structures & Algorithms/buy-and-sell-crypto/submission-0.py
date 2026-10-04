class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        n = len(prices)
        res = 0

        while (r < n):
            diff = prices[r] - prices[l]
            res = max(diff, res)
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                #prices[l] <= prices[r]
                r += 1
        return res
        