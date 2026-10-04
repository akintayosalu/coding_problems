class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        allNums = 0
        n = len(nums)
        for i in range(1,n+1):
            allNums = allNums ^ i

        currNums = 0
        for n in nums:
            currNums = currNums ^ n

        return allNums ^ currNums 

        