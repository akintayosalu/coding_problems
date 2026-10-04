class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []

        for i, highest_tmp in enumerate(temperatures):
            while stack and highest_tmp > stack[-1][0]:
                tmp, idx = stack.pop()
                res[idx] = i - idx
            
            stack.append((highest_tmp, i))

        return res
