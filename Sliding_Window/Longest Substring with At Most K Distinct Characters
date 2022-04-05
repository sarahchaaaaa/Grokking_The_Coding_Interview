class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s) * k == 0:
            return 0
        longestCount = 1
        letterDict = {}
        left = 0
        right = 0
        del_index = 0
        while right < len(s):
            letterDict[s[right]] = right
            right += 1
            
            if len(letterDict) == k + 1:
                delIndex = min(letterDict.values())
                del letterDict[s[delIndex]]
                left = delIndex + 1
            longestCount = max(longestCount, right - left)
        return longestCount
