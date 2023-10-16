def duplicate_nums(nums):
    count = {}
    for num in nums:
        count[num] = num not in count
    return sorted(list(filter(lambda x: not count[x],count.keys())))