class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Can I assume valid input?
        # what characters do I need to account for?
        # Are there bounds to the problem? Do I need to worry about overflow?
        # s = "abcdefc" -> abcdef
        # s = "pwfefk " -> pwfe
        # create a set that will keep track of the numbers that we've already seen and its index
        seenNum = {}
        # if we encounter a letter that already exists, then we shrink window from that index of the letter, update the index, take max of the prev max and the size of the new string
        currSub = ""
        maxCount = 0
        for count, letter in enumerate(s):
            if letter not in currSub:
                seenNum[letter] = count #{a:0, b:1}
                currSub += letter #ab
            else:
                currSub = s[seenNum[letter] + 1:count] + letter #b
                seenNum[letter] = count # {a:0, b:2}
            maxCount = max(len(currSub), maxCount) #123
        
        return maxCount
