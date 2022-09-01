#https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s = list(s)
        t = list(t)
        #first tidy the strings that are given 
        while s.count("#") >=1:
            
            idx = s.index("#")
            
            if idx == 0:
                s.pop(idx)
            else:
                s.pop(idx-1)
                s.pop(idx-1)
            
        while t.count("#") >=1:
            
            idx = t.index("#")
            
            if idx == 0:
                t.pop(idx)
            else:
                t.pop(idx-1)
                t.pop(idx-1)    
        
        
        #then compare two strings (lists)
        #if two strings are the same return True if not False  
        
        return s == t