from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_array = stones[:]
        if(len(new_array) == 1):
            return new_array[0]
        new_array = [-1*x for x in new_array]
        heapq.heapify(new_array)
        
        while(len(new_array) > 1 ):
            num1 = heapq.heappop(new_array)
            num2 = heapq.heappop(new_array)
            if(num1 != num2):
                out = -1*(num2 - num1)
                heapq.heappush(new_array,out)

        if(len(new_array) == 0):
            return 0 
        else:
            return -1*new_array[0]

                
s = Solution()
print(s.lastStoneWeight([3,7,2]))