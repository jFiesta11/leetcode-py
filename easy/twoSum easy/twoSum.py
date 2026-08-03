class Solution(object):
    def twoSum(self, nums, target):
        for indexi, i in enumerate(nums):
            for indexj,  j in enumerate(nums):
                if indexi == indexj:
                    continue
                elif (i+j) == target:
                    return indexi,indexj
                