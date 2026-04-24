from typing import List
import heapq
class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        nums = [-x for x in nums]
        n = len(nums)
        heap_array = []
        score = 0
        for i in range(n):
            heapq.heappush(heap_array,nums[i])
            if(s[i] == "1"):
                score += -1*heap_array[0]
                heapq.heappop(heap_array)
        return score
                
                    

s = Solution()
print(s.maximumScore([2,1,5,2,3],"01010"))