# 66 Plus One (Leetcode)
# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        #print(digits)
        
        length = len(digits)
        
        digits[length-1] = digits[length-1] +1
        
        #print(digits)
        
        for i in reversed(range(0,length)):
            if digits[i] >= 10:
                if i != 0:
                    digits[i] = 0
                    digits[i-1] = digits[i-1] + 1
                else:
                    digits[i] = 0
                    digits.insert(0,1)
                    
        return digits
