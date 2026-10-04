class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        sDict = dict()
        tDict = dict()

        for c in s:
            sDict[c] = sDict.get(c,0) + 1

        for c in t:
            tDict[c] = tDict.get(c,0) + 1

        return sDict == tDict

        