class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = dict()
        for i,n in enumerate(nums):
            dif = target - n
            if dif in idx:
                return [idx[dif],i]
            idx[n] = i

        return [0,0]