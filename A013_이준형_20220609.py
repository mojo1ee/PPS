#https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #need to use list.count(element) 
        
        if len(nums) == 1:
            return nums[0]
        
        else:
            for i in range(len(nums)):
                if nums.count(nums[i]) != 2:
                    return nums[i]