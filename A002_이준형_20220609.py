#118. Pascal's Triangle (LeetCode)
#https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        p = []
        coef = 1
        
        for i in range(numRows):
            p.append([])
            
        
        for i in range(1, numRows+1):
            for j in range(0, i):
                if j==0 or i==0:
                    coef = 1
                else:
                    coef = coef * (i -j)//j
                    
                p[i-1].append(coef)
            
        return p
