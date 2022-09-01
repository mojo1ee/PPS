#https://leetcode.com/problems/power-of-four/

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        # 1 ,4 ,16, 64, 256 
        
        if (n == 0):
            return False
        while (n != 1):
            if (n % 4 != 0):
                return False
            n = n // 4
             
        return True