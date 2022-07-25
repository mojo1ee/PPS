#https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        #get string length
        #split string into half (just did it with index)
        #traverse each word and count if inside vowels 
        #compare if two (vowel_counts) are the same 
        #return value 
        
        count = [0, 0]
        
        for i in range(len(s)):
            if (i+1) <= len(s) / 2:
                if s[i] in vowels:
                    count[0] += 1
            else:
                if s[i] in vowels:
                    count[1] +=1
        
        return count[0] == count[1]