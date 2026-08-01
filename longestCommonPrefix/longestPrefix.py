class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""

        for i in range(len(strs[0])):
            currentChar = strs[0][i]
            if all( i < len(c) and c[i] == currentChar for c in strs):
                result += currentChar 
        return result       