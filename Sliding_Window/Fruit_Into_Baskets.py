class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = right = 0
        fruitDict = {}
        maxTrees = 0
        while right < len(fruits):
            fruitDict[fruits[right]] = right
            right += 1
            if len(fruitDict) > 2:
                min_index = min(fruitDict.values())
                del fruitDict[fruits[min_index]]
                left = min_index + 1
            maxTrees = max(maxTrees, right - left)
        return maxTrees 
