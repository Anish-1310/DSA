def findMaxAverage(self, nums, k):
        window = sum(nums[:k])
        sums = window
        for i in range(k,len(nums)):
            window = window + nums[i] - nums[i-k]
            sums = max(window,sums)
        return sums/k