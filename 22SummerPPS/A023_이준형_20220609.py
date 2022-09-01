#https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        temp = str(num)
        sum_temp = 0
        
        while len(temp) >= 2:
            sum_temp = sum([int(char) for char in temp])
            temp = str(sum_temp)
        
        return int(temp)