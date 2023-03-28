def sum_range(nums, start=0, end=None):
    if end is None:
        end = len(nums)

    return sum(nums[start:end+1])
