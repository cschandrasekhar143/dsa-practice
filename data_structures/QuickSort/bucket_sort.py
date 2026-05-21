from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict.keys():
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        heap_list = []
        for key in freq_dict.keys():
            heap_list.append((freq_dict[key],key))
        heapq.heapify(heap_list)
        out_array = []
        for i in range(k):
            out_array.append(heapq.heappop(heap_list)[1])
        return out_array
sol = Solution()
sol.topKFrequent([1,1,1,2,2,3],2)