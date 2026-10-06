class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        seen = set()
        res = 0
        while (r < n):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                res = max(res, r-l)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

        return res

        