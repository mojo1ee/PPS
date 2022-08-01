# Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title/

class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        
        title = (title.lower()).split()
        
        for i in range(len(title)):
            if len(title[i]) > 2:
                if title[i].islower():
                    title[i] =  title[i].capitalize()
                
        
        title = " ".join(title)
        
        return title