class Solution:
    def isUgly(self, n):
        ugly=True
        factors=[2,3,5]
        if n<=0:
            ugly=False
        elif n==1:
            ugly=True
        else:
            for factor in factors:
                while n % factor == 0:
                    n /= factor
            if n > 1:
                ugly = False
        return ugly    