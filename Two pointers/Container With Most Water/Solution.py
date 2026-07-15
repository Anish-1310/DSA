def maxArea(self, height):
        l, r = 0, len(height)-1
        res = 0
        while l < r:
            h = min(height[l],height[r])
            water = (r-l)* h
            res = max(res,water)
            if height[l]< height[r]:
                l +=1
            else:
                r -=1
        return res