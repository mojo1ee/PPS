#https://leetcode.com/problems/sqrtx/

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        left, right = 0, x
        
        while left <= right:
            
            middle = (left+right)//2
            
            if middle * middle <= x < (middle+1) * (middle+1):
                return middle
            
            elif x < middle * middle:
                right = middle - 1
                
            else:
                #left = left+1
                left = middle + 1