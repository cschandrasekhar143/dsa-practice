# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List,Optional
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap_array = []
        i = 0
        tracker_array = [0]*len(lists)
        for list_array in lists:
            heap_array.append((list_array[0].val,i))
            i+=1
        heapq.heapify(heap_array)
        out_array = []
        while True:
            if(len(heap_array) == 0):
                break
            val = heapq.heappop(heap_array)
            out_array.append(lists[val[1]][tracker_array[val[1]]])
            heapq.heappush((lists[val[1]][tracker_array[val[1]]].next.val,val[1]))
            tracker_array[val[1]] += 1    