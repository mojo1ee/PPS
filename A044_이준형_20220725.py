# Student Attendance Record
# https://leetcode.com/problems/student-attendance-record-i/

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s.count('A') > 1:
            return False
        elif s.count('L') < 3:
            return True

        lateSequence = [1 if e == 'L' else 0 for e in s]
        
        consecutiveLateDays = 0
        
        for e in lateSequence: 
            if e == 0:
                consecutiveLateDays = 0
                continue
            elif e == 1:
                consecutiveLateDays += 1
                
            if consecutiveLateDays > 2:
                return False
            
        return True