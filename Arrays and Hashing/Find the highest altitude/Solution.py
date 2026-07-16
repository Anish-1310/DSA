def largestAltitude(self, gain):
        max_height = 0
        i = 0
        for g in gain:
            i += g
            max_height = max(max_height, i)
        return max_height