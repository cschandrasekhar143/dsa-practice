from typing import List
import heapq
class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        out1 = []
        out2 = []
        out2_pos = []
        for i in range(n):
            if(technique1[i] > technique2[i]):
                out1.append(technique1[i])
            else:
                out2.append(((technique2[i] - technique1[i]),i))
        score = 0    
        if(len(out1) >= k):
            score = sum(out1) + sum(technique2[x[1]] for x in out2)
        else:
            heapq.heapify(out2)
            for i in range((k-len(out1))):
                val = heapq.heappop(out2)
                score += technique1[val[1]]
            for i in range(len(out2)):
                score += technique2[out2[i][1]]
            score += sum(out1)
        return score
s = Solution()
#print(s.maxPoints([1000,900,800],[1,2,3],k=2))
print(s.maxPoints([1,2,3],[4,5,6],k=0))