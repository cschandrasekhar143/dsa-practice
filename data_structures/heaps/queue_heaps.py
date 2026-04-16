
from data_structures.heaps.heaps_master import MinPriorityQueue,MaxPriorityQueue

class Queue:
    def __init__(self):
        self.counter = 0
        self.mapping = {}
        self.min_priority_queue = MinPriorityQueue()

    def enqueue(self,k):
        self.counter += 1
        self.mapping[self.counter] = k
        self.min_priority_queue.min_heap_insert(self.counter)

    def dequeue(self):
        if self.min_priority_queue.length < 1:
            raise IndexError("Empty Queue")
        value = self.min_priority_queue.min_heap_extract_min()
        
        output = self.mapping[value]
        del self.mapping[value]
        if self.min_priority_queue.length < 1:
            self.counter = 0
        return output
    
    def peek(self):
        pass
    def rear(self):
        pass
    def isEmpty(self):
        if self.min_priority_queue.length < 1:
            return True
        else:
            return False
    def isFull(self):
        pass

class Stack:
    def __init__(self):
        self.counter = 0
        self.mapping = {}
        self.max_priority_queue = MaxPriorityQueue()

    def psuh(self,k):
        self.counter += 1
        self.mapping[self.counter] = k
        self.max_priority_queue.max_heap_insert(self.counter)

    def pop(self):
        if self.max_priority_queue.length < 1:
            raise IndexError("Empty Queue")
        value = self.max_priority_queue.max_heap_extract_max()
        
        output = self.mapping[value]
        del self.mapping[value]
        if self.max_priority_queue.length < 1:
            self.counter = 0
        return output

