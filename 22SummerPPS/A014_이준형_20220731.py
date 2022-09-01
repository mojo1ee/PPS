#https://leetcode.com/problems/summary-ranges/

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        if len(nums) ==0:
            return []
        
        start = nums[0]
        prev = ""
        answer = []


        for i in range(len(nums)):
            current = nums[i]

            if i == 0 or (current - prev) == 1:
                prev = current
            elif current - prev != 1:
                if prev == start:
                    answer.append(str(start))
                else:
                    answer.append(str(start) + '->' + str(prev))

                start = nums[i]
                prev = current 

            if i == len(nums)-1:
                if start == current:
                    answer.append(str(start))
                else:    
                    answer.append(str(start) + '->' + str(current))
                    
        return answer