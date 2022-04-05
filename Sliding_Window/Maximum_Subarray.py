class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSubarray = nums[0]
        maxTotal = nums[0]
        
        for num in nums[1:]:
            currSubarray = max(num, currSubarray + num)
            maxTotal = max(maxTotal, currSubarray)
        return maxTotal
