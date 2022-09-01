#https://leetcode.com/problems/valid-perfect-square/

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        #topic is binary search. 
            #if left == right then false? (sth like this)
        
        
        left, right = 0, num
        
        while left <= right:
            
            mid = (left+right) // 2
            
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid +1
            else:
                right = mid - 1
            
        return False