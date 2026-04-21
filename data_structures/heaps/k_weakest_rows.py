from typing import List
import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        sum_array = [] 

        for i in range(m):
            sum_array.append((sum(mat[i]),i))

        out_array = []
        heapq.heapify(sum_array)
        for i in range(k):
            out_array.append(heapq.heappop(sum_array)[1])
        return out_array