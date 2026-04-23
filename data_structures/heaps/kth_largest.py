from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_array = nums[:k]
        n = len(nums)
        heapq.heapify(heap_array)
        for i in range(k,n,1):
            if(heap_array[0] < nums[i]):
                heapq.heapreplace(heap_array,nums[i])
        return heap_array[0]