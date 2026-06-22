def containsDuplicate(self, nums) :
        dup = set()
        for i in nums:
            if i in dup:
                return True
            dup[i] = 1
        return False
