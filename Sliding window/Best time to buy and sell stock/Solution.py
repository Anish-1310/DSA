def maxProfit(self, prices) :
        mins = prices[0]
        maxs = 0
        for i in prices:
            if i < mins:
                mins = i
            else:
                profit = i - mins
                maxs = max(maxs, profit)
        return maxs