class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        n = len(temperatures)
        for i in range(n):
            lowest = temperatures[i]
            count = 0
            ans.append(count)
            for j in range(i+1, n):
                count += 1
                if temperatures[j] > lowest:
                    ans[i] = count
                    break

        return ans
                

        