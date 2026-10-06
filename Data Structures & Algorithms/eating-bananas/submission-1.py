class Solution:
    def calcHours(self, piles, k):
        tot = 0
        for p in piles:
            tot += math.ceil(p/k)
        return tot

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        res = hi

        while (lo <= hi):
            k = lo + (hi-lo)//2
            #Calculate the total hours it would take if k
            tot = self.calcHours(piles, k)
            
            #If total hours is less than h hours -> it is a possible res. 
            if tot <= h:
                res = min(res, k)
                #only look left for smaller possible k's
                hi = k - 1
            #Total hours is greater than h, so need bigger k -> search the right
            elif tot > h:
                lo = k + 1

        return res




    

        