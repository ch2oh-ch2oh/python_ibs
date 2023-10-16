def duplicate_nums(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] = False
        else:
            count[num] = True
        return sorted(list(filter(lambda x: not count[x],count.keys())))