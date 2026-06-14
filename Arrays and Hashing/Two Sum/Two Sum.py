def twoSum(self, nums, target):
    num_dict = {}
    for i,num in enumerate(nums):
        diff = target - num
        if diff in num_dict:
            return [i ,num_dict[diff]]
        num_dict[num] = i
    return[]