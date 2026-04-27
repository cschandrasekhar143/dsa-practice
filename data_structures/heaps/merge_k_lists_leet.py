# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap_array = []
        if(not lists):
            return None
        if all(sub is None for sub in lists):
            return None
        # Make heap elements in tuple format
        for i,list_array in enumerate(lists):
            if(list_array is None):
                continue
            heap_array.append((list_array.val,i,list_array))
        
        # Build heap
        heapq.heapify(heap_array)  

        # Extract and Swap 
        out_list = []
        while True:
            if(len(heap_array) == 0):
                break
            node = heap_array[0][2]
            out_list.append(node)
            next_node = node.next
            if(next_node is None):
                heapq.heappop(heap_array)
            else:
                swap_tuple = (next_node.val,heap_array[0][1],next_node)
                heap_array[0] = swap_tuple
                heapq._siftup(heap_array,0)
        n = len(out_list)
        
        for i,x in enumerate(out_list):
            if(i == (n-1)):
                x.next = None
                break
            x.next = out_list[i+1]
        return out_list[0]
