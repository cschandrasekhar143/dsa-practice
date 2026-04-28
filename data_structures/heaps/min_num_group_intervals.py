from typing import List
import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda x:x[0])  
        groups = []
        
        for interval in intervals:
            
            if len(groups) > 0 and interval[0] > groups[0]:
                groups[0] = interval[1]
                heapq._siftup(groups,0)        
            else:
                heapq.heappush(groups,interval[1])
            
        return len(groups)
