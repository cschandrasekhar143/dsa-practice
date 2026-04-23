from typing import List
import heapq
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        i = 0
        heapq.heapify(amount)
        while True:
            if(amount[0] == 0  and amount[1] == 0 and amount[2] ==0 ):
                break
            if (amount[1] != 0):
                amount[1] -= 1
            if (amount[2] != 0):
                amount[2]-= 1
            heapq.heapify(amount)
            i+=1
        return i 