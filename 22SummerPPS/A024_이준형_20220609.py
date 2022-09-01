#https://leetcode.com/problems/lemonade-change/

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        able = True
        
        count_5 = 0 #bills.count(5)
        count_10 = 0 #bills.count(10)
        count_20 = 0 #bills.count(20)
        
        
        #print(count_5, count_10, count_20)
        
        
        for bill in bills:
            if bill == 5:
                count_5 += 1
                
            elif bill == 10:
                count_5 -= 1
                count_10 += 1
                    
            elif bill == 20:
                if count_10 >=1: 
                    count_5 -= 1
                    count_10 -= 1
                else:
                    count_5 -= 3
                
                count_20 += 1
                        
            print(count_5, count_10, count_20)
            
            if count_5 < 0 or count_10 < 0 or count_20 <0:
                able = False
                return able
                
        return able