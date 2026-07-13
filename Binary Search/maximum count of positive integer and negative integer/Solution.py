def maximumCount(self, nums):
        pos_num = len(nums)- self.pos(nums)
        neg_num = self.neg(nums)
        return max(pos_num,neg_num)

def neg(self, nums):
    l, r = 0, len(nums)-1
    res = len(nums)
    while l<=r:
        m = (l+r)//2
        if nums[m]< 0:
            l = m+1
        else:
            res = m
            r = m -1
    return res
def pos(self, nums):
    l, r = 0, len(nums)-1
    res = len(nums)
    while l<=r:
        m = (l+r)//2
        if nums[m]<= 0:
            l = m+1
        else:
            res = m
            r = m -1
    return res