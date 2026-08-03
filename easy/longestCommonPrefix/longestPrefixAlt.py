class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""

        for i in zip(*strs):
            if(len(set(i) == 1)):
                result += strs[0][i]
            else:
                break
        return result