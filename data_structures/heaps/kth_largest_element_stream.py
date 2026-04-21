from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.n = len(nums)
        if(self.n !=0 ):
            if self.n < k:
                self.heap_array = self.nums[:]
                heapq.heapify(self.heap_array)
            else:
                self.heap_array = self.nums[0:k]
                heapq.heapify(self.heap_array)
                for i in range(k,self.n,1):
                    self.add(nums[i])

        else:
            self.heap_array = []

    def add(self, val: int) -> int:
        if(len(self.heap_array) < self.k):
            heapq.heappush(self.heap_array,val)
        else:
            if(self.heap_array[0] < val):
                heapq.heapreplace(self.heap_array,val)
        return self.heap_array[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)