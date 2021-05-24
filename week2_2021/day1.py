#11 container with most water
class SolutionWaterContainer:
    def maxArea(self, height: "List[int]") -> "int":
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res


#39 combination sum
class SolutionComboSum:
    def combinationSum(self, candidates: "List[int]", target: "int") -> "List[List[int]]":
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res


    def dfs(self, candidates, target, index, path, res):
        if target < 0:
            return

        if target == 0:
            res.append(path)
            return

        for i in range(index, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)
