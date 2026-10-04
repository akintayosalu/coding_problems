class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        i = 0
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                # print(i,j,k, tot)
                if tot == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    # while j < k and nums[k] == nums[k+1]:
                    #     k -= 1
                elif tot < 0:
                    j += 1
                    # while j < k and nums[j] == nums[j-1]:
                    #     j += 1
                elif tot > 0:
                    k -= 1
                    # while j < k and nums[k] == nums[k+1]:
                    #     k -= 1

            i += 1
            while (i < len(nums)) and nums[i] == nums[i-1]:
                i += 1

        return res
        