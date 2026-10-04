class Solution:
    def reverseBits(self, n: int) -> int:
        newN = 0
        count = 32
        while (count > 0):
            newN = newN << 1
            dig = n & 1
            newN = newN | dig
            n = n >> 1
            
            count -= 1

        return newN