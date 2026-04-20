import heapq
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap_array = [(-1*s,i) for i,s in enumerate(score)]   
        print(heap_array)     
        heapq.heapify(heap_array)

        print(heap_array)
        n = len(score)
        out_array = [""]*n
        for i in range(n):
            if(i == 0):
                max_element = heapq.heappop(heap_array)
                out_array[max_element[1]] = "Gold Medal"
                continue
            elif(i == 1):
                max_element = heapq.heappop(heap_array)
                out_array[max_element[1]] = "Silver Medal"
                continue  
            elif(i == 2):
                max_element = heapq.heappop(heap_array)
                out_array[max_element[1]] = "Bronze Medal"
                continue  
            else:
                max_element = heapq.heappop(heap_array)
                out_array[max_element[1]] = f"{i+1}"

        return out_array
    

x = Solution()
print(x.findRelativeRanks([5,4,3,2,1]))
             
