unsorted_nums = [0, 0, 0]
# sorted_nums = [-1, -1, 0, 1, 2, -4]
nums = sorted(unsorted_nums)


result = []

for i in range(len(nums)):
    # i left right
    left = i + 1
    right = len(nums) - 1

    while left < right:
        sumOfNums = sum([nums[i], nums[left], nums[right]])
        if sumOfNums == 0:
            result.append([nums[i], nums[left], nums[right]])
            if len(nums) != 3:
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            else:
                break
        elif sumOfNums < 0:
            left += 1
        else:
            right -= 1


print(result)
