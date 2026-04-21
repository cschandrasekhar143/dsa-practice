from typing import List
import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_array = [(num,i) for i,num in enumerate(nums)]
        heap_array = nums_array[:k]
        heapq.heapify(heap_array)
        for i in range(len(nums)-k):
            if(heap_array[0][0] < nums_array[k+i][0]):
                    heap_array[0] = nums_array[k+i]
                    heapq._siftup(heap_array,0)
        
        final_array = sorted(heap_array,key=lambda x:x[1])
        final_array = [x[0] for x in final_array]
        return final_array     


