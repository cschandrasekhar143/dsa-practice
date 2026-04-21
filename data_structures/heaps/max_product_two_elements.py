from typing import List
import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [(x - 1) for x in nums]
        max_two_array = nums[:2]
        
        heapq.heapify(max_two_array)
        for i in range(len(nums) - 2):
            if(nums[i+2] > max_two_array[0]):
                max_two_array[0] = nums[i+2]
                if(max_two_array[0] > max_two_array[1]):
                    max_two_array[0],max_two_array[1] = max_two_array[1],max_two_array[0]
                
        
        return  max_two_array[0]*max_two_array[1]