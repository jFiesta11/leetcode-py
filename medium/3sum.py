class Solution(object):
    def threeSum(self, nums):
        sortedNums = sorted(nums)
        result = []

        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            # [i, left, right]
            left = i + 1
            right = len(sortedNums) - 1
            while left < right:
                sumOfNums = sum([sortedNums[i], sortedNums[left], sortedNums[right]])
                if sumOfNums == 0:
                    result.append([sortedNums[i], sortedNums[left], sortedNums[right]])
                    left += 1
                    right -= 1
                    while left < right and sortedNums[left] == sortedNums[left - 1]:
                        left += 1
                    while left < right and sortedNums[right] == sortedNums[right + 1]:
                        right -= 1
                elif sumOfNums < 0:
                    left += 1
                else:
                    right -= 1

        return result
