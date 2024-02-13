class Solution:
    def moveZeroes( nums):
        sparshva = 0
        for king in range(len(nums)):
            if nums[king] != 0 and nums[sparshva] == 0:
                nums[sparshva], nums[king] = nums[king], nums[sparshva]

            
            if nums[sparshva] != 0:
                sparshva += 1