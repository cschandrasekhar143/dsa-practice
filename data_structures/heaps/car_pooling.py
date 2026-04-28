from typing import List
import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips = sorted(trips,key=lambda x:x[1])
        print(trips)
        var = 0
        heap_array = [(trip[2],trip[0]) for trip in trips]
        heapq.heapify(heap_array)
        num_passengers = 0
        n = len(trips)
        for i in range(n):
            start_point = trips[i][1]
            while(heap_array[0][0] <= start_point):
                val = heapq.heappop(heap_array)
                num_passengers -= val[1]
            num_passengers += trips[i][0]
            if(num_passengers > capacity):
                var = 1

        if(var == 1):
            return False
        else:
            return True
        

sol = Solution()
sol.carPooling([[9,3,6],[8,1,7],[6,6,8],[8,4,9],[4,2,9]],capacity=28)