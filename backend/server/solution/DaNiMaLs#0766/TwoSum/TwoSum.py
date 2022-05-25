def two_sum(nums, target):
    for x in range(len(nums)):
        for i in range(x + 1, len(nums)):
            if x + i == target:
                return [x, i]
