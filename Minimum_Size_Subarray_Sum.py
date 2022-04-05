class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minCount = math.inf
        left = 0
        right = 0
        total = 0
        
        while right < len(nums):
            total += nums[right]
            
            while total >= target:
                minCount = min(minCount, right-left+1)
                total -= nums[left]
                left += 1
            right += 1
        return minCount if minCount != math.inf else 0
