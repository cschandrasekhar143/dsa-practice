from typing import List
import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]    
        heapq.heapify(gifts)
        for i in range(k):
            gifts[0] = -1*int(math.sqrt(-1*gifts[0]) // 1)
            heapq._siftup(gifts,0)
        gifts = [-x for x in gifts]    
        return sum(gifts)
    
sol = Solution()

print(sol.pickGifts([25,64,9,4,100],4))