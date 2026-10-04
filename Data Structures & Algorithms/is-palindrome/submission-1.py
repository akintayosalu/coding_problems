class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while (l < r):
            left = s[l]
            right = s[r]
            while (l < r) and not left.isalnum():
                l += 1
                left = s[l]
            while (l < r) and not right.isalnum():
                r -= 1
                right = s[r]

            if left == right:
                l += 1
                r -= 1
                continue
            else:
                return False

        return True
        