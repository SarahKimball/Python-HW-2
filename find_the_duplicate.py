def find_the_duplicate(nums):
    """
    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None
    """
    num_set = set()
    for num in nums:
        if num in num_set:
            return num
        else:
            num_set.add(num)
    return None
