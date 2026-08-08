# twoPointer
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

for i in range(len(nums)):
    watch = i
    seek = i + 1

    while seek != (len(nums)):
        if nums[seek] == nums[watch]:
            seek += 1
        else:
            watch += 1
            nums[watch] = nums[seek]
            seek += 1

print(nums.index(max(nums)))
