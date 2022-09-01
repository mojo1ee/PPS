#https://leetcode.com/problems/longest-common-prefix/


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        length = min(list(map(len,strs)))
        
        if length < 1:
            return ""
        
        flag = 0
        idx = -1
         
        for i in range(length):
            cmpStr = strs[0][i]
            
            for word in strs:
                if word[i] != cmpStr:
                    flag = 1
                    break
            
            if flag == 1:
                idx = i
                break
                
            if i == length -1:
                idx = i+1
                break
        
        if idx == -1:
            return ""
        else:
            return strs[0][0:idx]