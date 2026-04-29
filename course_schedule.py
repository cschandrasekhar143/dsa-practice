from typing import List
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        end_times = sorted(courses,key=lambda x:x[1])
        accepted = []
        count = 0
        start_date = 0
        for course in end_times:
            start_date = start_date + course[0]
            if(start_date <= course[1]):
                count +=1
                heapq.heappush(accepted,-1*course[0])
            else:

                if(len(accepted) != 0):
                    if (course[0] < -1*accepted[0]):
                        start_date = start_date - (-1*accepted[0])
                        accepted[0] = -1*course[0]
                        heapq._siftup(accepted,0)
                    else:
                        start_date = start_date - course[0]
                else:
                    start_date = start_date - course[0]

        return count
                         
                
            
