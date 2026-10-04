class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while (n > 0):
            is1 = n & 1
            ones += is1
            n = n >> 1

        return ones