class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        skips = 0
        l = 0
        r = 0
        res = 0
        n = len(s) 
        
        while (r < n):
            if s[l] == s[r]:
                r += 1
            elif skips < k:
                r += 1
                skips += 1
            else:
                res = max(res, r-l)
                l = r
                skips = 0
        return max(res, r-l)