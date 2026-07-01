def isPalindrome(self, s):
        st = ""
        for c in s:
            if c.isalnum():
                st += c.lower()
        return st == st[::-1]