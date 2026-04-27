import heapq
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [-x for x in score]
        print(score)
        heapq.heapify(score)
        print(score)
'''
       out_array = []
       for i in range(len(score)):
           val = heapq.heappop(score)
           out_array.append(f"i+1")
'''
x = Solution()
print(x.findRelativeRanks([5,4,3,2,1]))
             
