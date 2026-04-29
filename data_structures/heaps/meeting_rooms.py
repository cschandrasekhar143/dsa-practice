from typing import List
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings,key = lambda x:x[0])
        
        heap_array = []
        
        available_rooms_heap = [x for x in range(n)]
        heapq.heapify(available_rooms_heap)
        count_dict = [0] * n
        
        for i in range(len(meetings)):
            while True:
                if(len(heap_array) == 0):
                    break
                if(meetings[i][0] >= heap_array[0][0]):
                    val = heapq.heappop(heap_array)
                    heapq.heappush(available_rooms_heap,val[1])
                else:
                    break
            
            if len(available_rooms_heap) == 0:
                heap_array[0] = ((heap_array[0][0] + meetings[i][1] - meetings[i][0]) ,heap_array[0][1])
                count_dict[heap_array[0][1]] += 1
                heapq._siftup(heap_array,0)
            else:
                val = heapq.heappop(available_rooms_heap)
                heapq.heappush(heap_array,(meetings[i][1],val))
                count_dict[val] += 1
            
        count_heap  = [(-x,i) for i , x in enumerate(count_dict)]
        heapq.heapify(count_heap)
        return count_heap[0][1]
    

sol = Solution()
print(sol.mostBooked(3,[[1,20],[2,10],[3,5],[4,9],[6,8]]))

