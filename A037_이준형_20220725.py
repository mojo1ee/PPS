#https://leetcode.com/problems/self-dividing-numbers/

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        sdn = []
        
        for i in range(left,right+1):
            flag = 1
            number = str(i)
            
            
            if '0' in number:
                continue
                
            elif len(number) == 1:
                sdn.append(int(number))
                continue
                
            else: 
                for j in range(len(number)):
                    if int(number) % int(number[j]) != 0:
                        flag = 0
                        break
                        
            if flag == 1:
                sdn.append(i)
        
        return sdn