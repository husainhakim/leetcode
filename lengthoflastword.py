class Solution:
    def lengthOfLastWord(self, s):
       
        words = s.split()

        if words:
            lastword = words[-1]
            lenlastword = len(lastword)
            return lenlastword
        else:
            return 0 