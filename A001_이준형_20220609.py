#455. Assign Cookies (LeetCode)
#https://leetcode.com/problems/assign-cookies/

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        g.sort()
        s.sort()
        
        count = 0
        check = 0
        
        for greed in g:
            check = 0
            
            for size in s:
                if greed <= size:
                    count = count + 1
                    s.remove(s[s.index(size)])
                    check = 1
                    break
                    
            if check == 0 or len(s) == 0 :
                break
        
        return count
