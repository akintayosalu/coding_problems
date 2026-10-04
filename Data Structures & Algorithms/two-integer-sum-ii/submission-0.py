class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while (l < r):
            n1 = numbers[l]
            n2 = numbers[r]
            tot = n1+n2

            if tot == target:
                return [l+1, r+1]
            elif tot < target:
                l += 1
            else:
                #tot > target
                r -= 1

        return [0,0]
        